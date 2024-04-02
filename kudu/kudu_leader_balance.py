'''
create_time: 2024/3/28 17:21
author: yss
version: 1.0
'''
# Do best effort to make one/more/all table(s) leaders balanced.
import subprocess
import sys
import time

from collections import defaultdict


def ksck(master_addresses) :
    ksck_cmd = 'sp_kudu cluster ksck %s -ksck_format=plain_full' % master_addresses
    ksck_output = subprocess.check_output(ksck_cmd, shell=True, stderr=subprocess.STDOUT)
    ksck_lines = ksck_output.decode('utf-8').split('\n')  #ksck 结果列表
    return ksck_lines


def scheduling_uno_op(master_addresses, op) :
    tablet, leader = op
    step_down_cmd = 'sp_kudu tablet leader_step_down %s %s -new_leader_uuid=%s' % (master_addresses, tablet, leader)
    print('scheduling: ', step_down_cmd)
    subprocess.check_output(step_down_cmd, shell=True, stderr=subprocess.STDOUT)


def parse_ksck(ksck_lines, table_filter):
    idx = 0
    ts_map = defaultdict(list)  #创建一个字典，默认值是列表
    tablet_tuple_list = list()
    while idx < len(ksck_lines): #遍历每一行
        line = ksck_lines[idx]
        tablet_id, table = '', ''
        # e.g. Tablet 288b5b776eb84f0f9b1f32163be5870b of table 'profile_wos_p2' is healthy.
        if 'Tablet' in line and 'of table' in line:
            tablet_id = line.split(' ')[1]
            table = line.split(' ')[4][1 :-1]
            idx += 1
        else:
            idx += 1
            continue
        if table not in table_filter:
            continue

        # 通过两个 if 找到匹配的表
        leader_ts = ''
        all_ts_of_tablet = []
        ts_id = ''

        # To parse the tablet ts mapping info e.g.
        #   a1cbc1e51e6e43d9be09bea38c3fade3 (debugboxreset1775x3.sa:7050): RUNNING [LEADER]
        #   e1919bbab5f544128aab6215451583a9 (debugboxreset1775x2.sa:7050): RUNNING
        #   b5d3cd51688a4af1a25a6d5c9ba4c840 (debugboxreset1775x1.sa:7050): RUNNING
        while ksck_lines[idx].startswith('  '):
            if not 'RUNNING' in ksck_lines[idx] or 'NONVOTER' in ksck_lines[idx] :
                idx += 1
                continue
            ts_id = ksck_lines[idx].strip().split(' ')[0]
            all_ts_of_tablet.append(ts_id)   #取出该tablet 所在的 tserver uuid
            ts_map[ts_id]  # access make all ts is in map   ts_map  {ts_id:[],ts_id1:[]}

            if ksck_lines[idx].endswith('[LEADER]') :
                ts_map[ts_id].append(tablet_id)
                leader_ts = ts_id
            idx += 1
        if len(all_ts_of_tablet) != 3:
            del ts_map[ts_id]
        else:
            tablet_tuple_list.append((tablet_id, leader_ts, all_ts_of_tablet))

        # ts_map 里面包括 tserver uuid 为 key组成的字典，值是一个列表，只有 ledaer 所在的 tserver uuid 列表有值
    return tablet_tuple_list, ts_map


def cal_mean(ts_map):
    all_cnt = sum([len(_) for _ in ts_map.values()])  #所有的 tablet_leader 有多少
    ts_cnt = len(ts_map)  #有多少个 tserver
    mean_cnt = all_cnt / ts_cnt  #每个 tablet 应该分多少
    return mean_cnt


def eval_score(ts_map) :
    # true -> balanced
    mean_cnt = cal_mean(ts_map)
    score = sum([((len(_)) - mean_cnt) ** 2 for _ in ts_map.values()])
    return score, score < 1


def print_skew_info(ts_map) :
    mean_cnt = cal_mean(ts_map)
    for ts, v in ts_map.items() :
        skew_value = len(v) - mean_cnt
        if abs(skew_value) < 1 :  # balanced
            print('ts %s has %d avg is %f' % (ts, len(v), mean_cnt))
            continue
        elif skew_value > 0 :
            print('ts %s execceds %f' % (ts, skew_value))
        else:
            print('ts %s behinds %f' % (ts, skew_value))


reached = False
best_op = [float("inf"), []]


# op = (tablet, leader)
def dfs(tablet_tuple_list, ops, leader_map, mean_cnt):
    global best_op, reached
    sorted_ts_list = sorted(leader_map.items(), key=lambda x: len(x[1]))
    if reached:
        return
    if len(tablet_tuple_list) == 0:
        score, _ = eval_score(leader_map)
        if score < best_op[0]:
            best_op[0], best_op[1] = score, ops[: :]  # deep clone into result
            if score < 1:
                reached = True
        return
    tablet_id, leader, ts_list = tablet_tuple_list.pop()
    for ts, tablets in sorted_ts_list:
        if ts in ts_list:
            leader_map[ts].append(tablet_id)
            if leader != ts:
                ops.append((tablet_id, ts))
            dfs(tablet_tuple_list, ops[: :], leader_map, mean_cnt)
            if leader != ts :
                ops.pop()
            leader_map[ts].remove(tablet_id)


def solution(master_addresses, table_filter) :
    ksck_output = ksck(master_addresses)
    tablet_tuple_list, ts_map = parse_ksck(ksck_output, table_filter)
    score, balanced = eval_score(ts_map)
    print('current skew info')
    print_skew_info(ts_map)

    if balanced :
        print('table %s is rebalanced' % ':'.join(table_filter))
        return 0
    else:
        print('looking for solution')
        leader_map = defaultdict(list)
        for ts in ts_map.keys():
            leader_map[ts]  # just access and gen default
        dfs(tablet_tuple_list, [], leader_map, cal_mean(ts_map))
        global best_op
        print(best_op[0])
        print(best_op[1])
        for op in best_op[1] :
            scheduling_uno_op(master_addresses, op)
        try_time = 0
        has_to_try = True
        print('gathering info')
        while try_time < 5 and has_to_try :
            has_to_try = not try_and_gen_score(master_addresses)
            try_time += 1
        return 1 if has_to_try else 0


def try_and_gen_score(master_addresses) :
    try:
        time.sleep(5)
        print('waiting for skew info after gen')
        ksck_output = ksck(master_addresses)
        tablet_tuple_list, ts_map = parse_ksck(ksck_output, table_filter)
        score, balanced = eval_score(ts_map)
        print('after rebalance skew map')
        print_skew_info(ts_map)
        return score < 1
    except :
        print('cluster not rebalance done, waiting')
        return False


if __name__ == '__main__' :
    master_address, table_str = sys.argv[1], sys.argv[2]
    table_filter = table_str.split(',')   #把字符串转换成列表
    ret = solution(master_address, table_filter)
    sys.exit(ret)