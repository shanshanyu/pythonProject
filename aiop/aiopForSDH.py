#coding: utf-8
import argparse
import logging
import datetime
import sys
from collections import namedtuple
import getpass
import subprocess
import requests
import json
import prettytable
from hyperion_client.deploy_topo import DeployTopo
from hyperion_client.hyperion_inner_client.inner_directory_info import InnerDirectoryInfo

# 定义颜色
colorDefine = namedtuple(
    'colorDefine', ['red_color', 'green_color', 'yellow_color','dark_green', 'end_color','back_one_line','clear_one_line'])
color = colorDefine('\33[4;31;43m', '\33[1;32m', '\33[0;33m','\033[36m', '\033[0m','\033[F','\033[K')

csv_file="/home/sa_cluster/tag.csv"

VERSION = '250603'

def init_logger(logger_name,console_level=logging.INFO):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_name = '{}_{}.log'.format(logger_name, timestamp)
    log_path = '{}/{}'.format('/tmp', log_name)
    file_format = '%(asctime)s %(levelname)s %(message)s'
    console_format = f'{color.green_color}%(asctime)s %(levelname)s %(message)s{color.end_color}'

    #global config  日志记录器
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    #console config  日志处理器
    console = logging.StreamHandler()
    console.setLevel(console_level)
    console.setFormatter(logging.Formatter(console_format))
    logger.addHandler(console)

    #file config 日志处理器
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(file_format))
    logger.addHandler(fh)

    return logger

def get_ssh_info():
    hosts_list = DeployTopo().get_all_host_list()
    port_list = []
    get_port_list = run_cmd('sudo grep -w Port /etc/ssh/sshd_config')['stdout'].strip().split('\n')
    for sp in get_port_list:
        if sp.startswith('Port'):
            ssh_port = int(sp.split()[1])
            port_list.append(ssh_port)
    if len(port_list) == 0 or 22 in port_list:
        return 22, hosts_list
    return port_list[0], hosts_list

def run_cmd(cmd, timeout=300):
    process = subprocess.Popen(
        cmd,
        shell=True,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    try:
        (stdout, stderr) = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        print('run [{}] TIMEOUT'.format(cmd), file=sys.stderr)
        process.kill()
        (stdout, stderr) = process.communicate()
    ret = process.returncode
    res = {'cmd': cmd, 'ret': ret, 'stdout': stdout, 'stderr': stderr}
    return res

def op_guide():
    guide_table = prettytable.PrettyTable(
        field_names=['序号', '磁盘类型', '说明', '处理方案'])
    aiop_cf = "https://doc.sensorsdata.cn/pages/viewpage.action?pageId=304047773"
    guide_table.title = (f"操作指引大全 {aiop_cf}")
    guide_info = {1: ['系统盘(/)', '用于存放操作系统', '参考 3.1.1 处理'],
                  2: ['元数据盘(data or metadata)', '用于存放元数据信息及各个模块日志', '参考 3.1.2 处理'],
                  3: ['随机数据盘(rnddata)', '用于存放 kudu 用户数据,skv 用户关联数据', '参考 3.1.3 处理'],
                  4: ['顺序盘(seqdata)', '用于存放 hdfs 事件数据,kafka 数据', '参考 3.1.4 处理'],
                  5: ['暂存盘(stdata)', '用于存放 nginx 接收环节的数据', '参考 3.1.5 处理'],
                  6: ['混合盘(hybriddata)', '用于存放 nginx,kudu,hdfs,kafka 数据', '参考 3.1.6 处理']
                  }
    guide_table.align = 'l'

    for k, v in guide_info.items():
        guide_table.add_row([k, v[0], v[1], v[2]])
    print(color.green_color +
          f"下述操作指引,需要我们一起使用并完善它!" + color.end_color)

def hdfs_du_info(d='/'):
    result = []
    hdfs_cmd = "sudo -u hdfs hdfs dfs -du -s -h" if len((run_cmd(
        "grep hdfs /etc/passwd|awk -F: '{print $1}'")['stdout'].split())) == 1 else "hdfs dfs -du -s -h"
    ls_cmd_info = f"hdfs dfs -ls {d}" + "|grep -v system|awk '/^d/'|awk '{print $NF}'"
    dirs = run_cmd(ls_cmd_info)['stdout'].split()
    for i in range(0, len(dirs)):
        tmp = run_cmd(
            f"{hdfs_cmd} {dirs[i]}|egrep -w 'G|T'")['stdout'].split()
        res = [data for data in tmp if float(tmp[0]) != 0 and len(tmp) != 0]
        if len(res) > 0:
            result.append(res)
    return result

def get_hdfs_du_info():
    hdfs_disk_table = prettytable.PrettyTable(field_names=['HDFS 目录', '大小(G)', '副本数'])
    hdfs_disk_table.title = ("HDFS 占用一览表")
    hdfs_disk_table.align = 'l'
    result = hdfs_du_info()
    result.extend(hdfs_du_info('/sa'))
    for i in result:
        if i[1] == 'T':
            i[0], i[1] = round(float(i[0]) * 1024, 1), 'G'
        if i[3] == 'T':
            i[2], i[3] = round(float(i[2]) * 1024, 1), 'G'
        hdfs_replica_info = 'normal' if (float(i[2]) / float(
            i[0])) < 5 else f'{color.red_color}abnormal{color.end_color}{color.green_color}'
        hdfs_disk_table.add_row([i[4], i[2], hdfs_replica_info])
    return hdfs_disk_table.get_string(sortby='HDFS 目录')

def get_disk_increase():
    metricDefine = namedtuple('promQlDefine', ['totaldisk', 'freedisk', 'job', 'mountpoint'])
    metric = metricDefine('node_filesystem_size_bytes',
                          'node_filesystem_free_bytes', 'sensors-inf-component',
                          '.data.*|.sensorsmounts.*|.kudu.*|.kafka.*')
    promQl = f'{{job="{metric.job}",mountpoint=~".*{metric.mountpoint}.*"}}'
    prometheus_host = DeployTopo().get_host_list_by_module_name('sm', 'prometheus')[0]
    #获取过去 10 天的最大
    disk_urls = (f'http://{prometheus_host}:8310/api/v1/query?query=max_over_time({metric.freedisk}{promQl}[10d])',
                 f'http://{prometheus_host}:8310/api/v1/query?query={metric.freedisk}{promQl}',
                 f'http://{prometheus_host}:8310/api/v1/query?query={metric.totaldisk}{promQl}')
    response = {
        'disk_before_free': requests.get(url=disk_urls[0]), #10天前的剩余空间
        'disk_now_free': requests.get(url=disk_urls[1]),   #现在的剩余空间
        'total_disk': requests.get(url=disk_urls[2])     #总的空间
    }
    results = {}
    for k, v in response.items():
        if v:
            tmp = (
                list(zip(([data['metric']['mountpoint'] for data in json.loads(v.content.decode())['data']['result']]),
                         [data['value'] for data in json.loads(v.content.decode())['data']['result']])))
            results[k] = tmp
    return results

def get_disk_info(disk_threshold, if_print_detail, disk_name,logger):
    port = get_ssh_info()[0]
    disk_infos = []
    dir_used = []
    dir_table = prettytable.PrettyTable(
        field_names=['主机地址', '主机名称', '挂载点', '目录占用 TOP10', '占用'])
    df_cmd = f"df -Th|grep -E '{disk_name[0]}'|grep -Ev 'tmpfs|docker/overlay2'" + \
             "|awk '{print $(NF-6),$(NF-5),$(NF-4),$(NF-3),$(NF-2),$(NF-1),$(NF)}'|awk  '{if($1 != \"Type\") print($0)}'"
    for host_name in get_ssh_info()[1]:
        # host_info = re.split(' |\t', run_cmd(f"grep -w {host_name} /etc/hosts|grep -v '#'")['stdout'].strip())
        host_info = run_cmd(
            f"grep -w {host_name} /etc/hosts|grep -v '#'")['stdout'].strip().split()
        disk_info = run_cmd(
            f"ssh {host_name} -p {port} {df_cmd}")['stdout'].strip().split('\n')
        disk_table = prettytable.PrettyTable(
            field_names=['序号', '主机地址', '主机名称', '分区类型', '挂载设备', '挂载点', '磁盘大小', '已用空间',
                         '可用空间', '磁盘使用率'])
        if len(''.join(disk_info)) > 1:
            for eachnode in disk_info:
                eachnode = eachnode.split()
                if int(eachnode[5].strip('%')) > disk_threshold[0]:
                    disk_infos.append(host_info[0:2] + eachnode)
                    if if_print_detail == 'yes':
                        dir_used.append(
                            run_cmd(f"ssh {host_name} -p {port} 'sudo du -ahx {eachnode[6]} | sort -rhu | head -10'")[
                                'stdout'].strip().replace('\t', ':').split('\n'))

    if len(dir_used) > 0:
        for info, disk_info in zip(enumerate(disk_infos), dir_used):
            disk_table.add_row(
                [info[0] + 1, info[1][0], info[1][1], info[1][3], info[1][2], info[1][8], info[1][4], info[1][5],
                 info[1][6], info[1][7]])
            for dir in (disk_info):
                tmp = info[1][0:2] + dir.split(':')[::-1]
                try:
                    dir_table.add_row([tmp[0], tmp[1], info[1][8], tmp[2], tmp[3]])
                except:
                    print(
                        f'{color.red_color}磁盘{[info[1][8]]}性能拉跨亦或是该目录下有过多的碎文件导致无法获取目录占用 TOP!{color.end_color}')

    else:
        if len(disk_infos) > 0:
            for seq, info in enumerate(disk_infos):
                disk_table.add_row(
                    [seq + 1, info[0], info[1], info[3], info[2], info[8], info[4], info[5], info[6], info[7]])
        else:
            sys.exit(
                color.red_color + "未能获取到符合条件的磁盘!" + color.end_color)

    dir_table.align, disk_table.align = "l", "l"
    disk_table.title = ("磁盘使用率一览表")

    logger.info(f"磁盘使用率一览表.\n{disk_table.get_string(sortby=('序号'))}")
    if if_print_detail == 'yes':
        logger.info(f"目录占用 TOP10 统计完成,见下表.\n{dir_table}")
    op_guide()

def single_disk_evaluate(logger):
    '''单机磁盘扩容评估'''
    simple_suggest_list = []
    disk_info = "df -Th|grep -Ev 'tmpfs|overlay|Filesystem' | awk '$6+0 > 75 {print $7}'"
    disk_names = run_cmd(disk_info)['stdout'].strip().split()
    if not disk_names:
        sys.exit(color.yellow_color + "未找到符合规则的磁盘:\n1:磁盘使用率未超过 80%.\n2:磁盘名称不存在."+color.end_color)
    dir_reg = '|'.join(disk_names)
    all_disk_info = list(zip(get_disk_increase().get('disk_before_free'), get_disk_increase().get('disk_now_free'),
                             get_disk_increase().get('total_disk')))
    # {'disk_name':['disk_used','now_disk','total']}
    current_disk_info = {
        disk_info[0][0]: [(int(disk_info[0][1][1]) - int(disk_info[1][1][1])) / 1024 ** 3, int(disk_info[1][1][1]),
                          int(disk_info[2][1][1])] for disk_info in all_disk_info if disk_info[0][0] in disk_names}
    for k, v in current_disk_info.items():
        disk_used_rate_by_day = v[0] / 10
        expected_for_use = 30 * 12 * round(v[0] / 10)
        current_available = (0.9 * v[1] / 1024 ** 3) / disk_used_rate_by_day
        simple_suggest_list.append(
            f"# 现状:当前环境 {k} 盘,共 {round(v[2] / 1024 ** 3, 1)}G,使用率较高,详情见下述「磁盘使用率一览表」.\n# 方案:\n    ➤ 按照当前每天 {round(disk_used_rate_by_day, 2)}G 的增长情况估算,若将 {k} 扩 {expected_for_use}G,预计可使用 12 个月,磁盘剩余 {round(v[1] / 1024 ** 3)}G,距离到达 90% 预计还可使用 {round(current_available)} 天.\n")
    simple_suggest_list_to_str = ''.join(simple_suggest_list)
    if len(simple_suggest_list) > 0:
        suggestions = f"""
    ========================================磁盘扩容需积极========================================

    {simple_suggest_list_to_str}

    ========================================故障丢数不可取========================================

    """
        logger.info("正在获取 hdfs 中各个目录的使用情况,请稍后...")
        logger.info(
            f"下述「HDFS 占用一览表」需关注如下情况\n1:若非[/sa/data]目录较大,需要具体确认子目录使用情况,如果用不到可以删除释放部分存储\n2:副本数一列若出现[abnormal]请反馈给到「AIOP 工单整治」群\n{get_hdfs_du_info()}")
        logger.info(f"现状及扩容方案如下.\n{suggestions}")
    else:
        logger.info("很棒,当前环境的磁盘无需扩容!")
    get_disk_info([0],'yes',[dir_reg],logger)



def cluster_disk_evaluate():
    '''集群磁盘扩容评估'''
    pass


def disk_evaluate(logger):
    host_list = get_ssh_info()[1]
    if len(host_list) == 1:
        logger.info('当前是单机环境,正在获取磁盘使用情况及扩容方案,请稍后...')
        single_disk_evaluate(logger)
    elif len(host_list) == 3:
        logger.info('当前是 3 节点迷你集群,正在获取磁盘使用情况及扩容方案,请稍后...')
        cluster_disk_evaluate()
    else:
        logger.info(f'当前是 3+{len(host_list)-3}集群，正在获取磁盘使用情况及扩容方案,请稍后...')
        cluster_disk_evaluate()


def display_tag_info(logger):
    pass



def main():
    logger = init_logger('aiopForSDH',console_level=logging.INFO)
    logger.info(f'工具版本号:{VERSION}')
    #获取用户登录名
    if getpass.getuser() != 'sa_cluster':
        sys.exit("please use sa_cluster account.")

    parser = argparse.ArgumentParser()
    parser.add_argument('-e',action='store_true',default=False,help = 'evaluate disk')
    parser.add_argument('-d',action='store_true',default=False,help = 'display user_group or user_tag info')
    args = parser.parse_args()

    if args.e:
        disk_evaluate(logger)
    elif args.d:
        display_tag_info(logger)
    else:
        sys.exit(color.red_color+f'please input one valid argument at least'+color.end_color)



if __name__ == '__main__':
    main()