# -*-coding:utf-8 -*-

"""
# File       : aiopDisk.py
# Author     ：wangqing001
# Description：
# Revision History:
 Version       Author(s)          YYYY-MM-DD   Comments
 v1.0          wangqing001        2021-10-28   Initial version
 v1.1          wangqing001        2021-11-05   吐出分群被删了,但是存储没释放的情况.
 v1.2          wangqing001        2022-07-06   分群执行情况及未成功原因展示.
 v1.3          wangqing001        2022-09-06   新增磁盘使用率及占用 TOP 功能,并修复了一些bug.
 v1.4          wangqing001        2022-11-27   新增磁盘扩容评估功能.   
 v1.5          wangqing001        2023-05-08   新增按照日期获取 event 占用情况.
 v1.6          wangqing001        2023-07-12   重构了单机环境磁盘评估,支持单机环境指定磁盘评估.
"""


import argparse
import csv
import datetime
import getpass
import json
import logging
import os
import re
import subprocess
import sys
from collections import namedtuple
from functools import reduce

import prettytable
import requests

# 定义颜色

colorDefine = namedtuple(
    'colorDefine', ['red_color', 'green_color', 'yellow_color','dark_green', 'end_color','back_one_line','clear_one_line'])
color = colorDefine('\33[4;31;43m', '\33[1;32m', '\33[0;33m','\033[36m', '\033[0m','\033[F','\033[K')

try:
    from hyperion_client.deploy_topo import DeployTopo
    from hyperion_client.hyperion_inner_client.inner_directory_info import \
        InnerDirectoryInfo
except:
    pass
    #sys.exit(color.red_color+"该环境 SP 版本较低,建议推动升级!"+color.end_color)

# 工具版本号
VERSION='V2404'
# 设置日志
LOG_FORMAT = f"{color.green_color}[%(asctime)s] - [%(levelname)s] - %(message)s{color.end_color}"
FILE_NAME = "/home/sa_cluster/aiop_result.log"
LOGGER = logging.getLogger('mylog')
FH = logging.FileHandler(FILE_NAME)
SH = logging.StreamHandler()
FM = logging.Formatter(LOG_FORMAT)
FH.setFormatter(FM)
SH.setFormatter(FM)
LOGGER.addHandler(FH)
LOGGER.addHandler(SH)
LOGGER.setLevel(logging.INFO)


csv_file="/home/sa_cluster/tag.csv"

def log(parameter):
    def wrapper(func):
        def inner(*args, **kwargs):
            info = {
                'get_disk_info': '开始获取磁盘使用情况.',
                'get_customer_info': '开始获取当前环境基本信息.',
                'get_tag_disk': '开始获取当前环境分群/标签占用磁盘情况.',
                'get_user_tag_info': '开始获取当前环境分群运行情况.',
                'get_event_size_by_time':'开始获取当前环境事件占用情况.'
            }
            if parameter in info:
                LOGGER.info(f"{info[parameter]}")
            func(*args, **kwargs)
        return inner
    return wrapper


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

# 获取 ssh 信息


def _get_ssh_info():

    hosts_list = DeployTopo().get_all_host_list()
    ssh_port = 22
    port_list = []
    get_port_list = run_cmd(
        'sudo grep -w Port /etc/ssh/sshd_config')['stdout'].strip().split('\n')
    for sp in get_port_list:
        if sp.startswith('Port'):
            ssh_port = int(sp.split()[1])
            port_list.append(ssh_port)
    if len(port_list) == 0 or 22 in port_list:
        return 22, hosts_list
    return port_list[0], hosts_list

# 时间转换
def _time_trans(inputtime=datetime.datetime.now().strftime('%Y-%m-%d')):
    """_summary_

    Args:
        inputtime (string, optional):inputtime 待解析的时间.

    Returns:
        int: 返回转换后的天数格式
    """
    reg_check = re.compile('^\d{4}-\d{2}-\d{2}')
    if not reg_check.search(inputtime):
        return False
    hdfs_day = (datetime.datetime.strptime(inputtime,'%Y-%m-%d') - datetime.datetime(1970,1,1)).days
    return hdfs_day

# 客户信息，暂时只支持有 spadmin 命令的环境，后续再做适配
@log('get_customer_info')
def _get_customer_info() -> list:
    
    customer_infos = []
    table_normal = prettytable.PrettyTable(
        field_names=['客户ID', '过期时间', '是否单机', '节点个数'])
    item_info = ('customer_id', 'expire_time',
                 'simplified_cluster')
    node_count = len(DeployTopo().get_all_host_list())
    for info in item_info:
        value = run_cmd(
            f'spadmin config get global -n {info} -c')['stdout'].strip().split(' ')
        customer_infos.append(value[0].strip('"'))
    table_normal.add_row(
        [customer_infos[0], customer_infos[1], customer_infos[2], node_count])
    table_normal.align = "l"
    
    LOGGER.info(f"客户信息如下表:\n{table_normal}" )


def _guide():
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
          f"下述操作指引,需要我们一起使用并完善它!"+color.end_color)

# 各个节点磁盘使用情况及目录占用


@log('get_disk_info')
def _get_disk_info(disk_threshold, if_print_detail, disk_name):
    """
    获取磁盘使用情况
    :param disk_threshold:  # 磁盘使用率
    :param if_print_detail:  # 是否打印TOP10
    :param disk_name:  # 要匹配的磁盘名称
    """

    port = _get_ssh_info()[0]
    disk_infos = []
    dir_used = []
    dir_table = prettytable.PrettyTable(
        field_names=['主机地址', '主机名称', '挂载点', '目录占用 TOP10', '占用'])
    df_cmd = f"df -Th|grep -E '{disk_name[0]}'|grep -Ev 'tmpfs|docker/overlay2'" + \
        "|awk '{print $(NF-6),$(NF-5),$(NF-4),$(NF-3),$(NF-2),$(NF-1),$(NF)}'|awk  '{if($1 != \"Type\") print($0)}'"
    for host_name in _get_ssh_info()[1]:
        # host_info = re.split(' |\t', run_cmd(f"grep -w {host_name} /etc/hosts|grep -v '#'")['stdout'].strip())
        host_info = run_cmd(
            f"grep -w {host_name} /etc/hosts|grep -v '#'")['stdout'].strip().split()
        disk_info = run_cmd(
            f"ssh {host_name} -p {port} {df_cmd}")['stdout'].strip().split('\n')
        disk_table = prettytable.PrettyTable(
            field_names=['序号', '主机地址', '主机名称', '分区类型', '挂载设备', '挂载点', '磁盘大小', '已用空间', '可用空间', '磁盘使用率'])
        if len(''.join(disk_info)) > 1:
            for eachnode in disk_info:
                eachnode = eachnode.split()
                if int(eachnode[5].strip('%')) > disk_threshold[0]:
                    disk_infos.append(host_info[0:2]+eachnode)
                    if if_print_detail == 'yes':
                        dir_used.append(run_cmd(f"ssh {host_name} -p {port} 'sudo du -ahx {eachnode[6]} | sort -rhu | head -10'")[
                            'stdout'].strip().replace('\t', ':').split('\n'))

    if len(dir_used) > 0:
        for info, disk_info in zip(enumerate(disk_infos), dir_used):
            disk_table.add_row(
                [info[0]+1, info[1][0], info[1][1], info[1][3], info[1][2], info[1][8], info[1][4], info[1][5], info[1][6], info[1][7]])
            for dir in (disk_info):
                tmp = info[1][0:2]+dir.split(':')[::-1]
                try:
                    dir_table.add_row([tmp[0], tmp[1], info[1][8], tmp[2], tmp[3]])
                except:
                    print(f'{color.red_color}磁盘{[info[1][8]]}性能拉跨亦或是该目录下有过多的碎文件导致无法获取目录占用 TOP!{color.end_color}')

    else:
        if len(disk_infos) > 0:
            for seq, info in enumerate(disk_infos):
                disk_table.add_row(
                    [seq+1, info[0], info[1], info[3], info[2], info[8], info[4], info[5], info[6], info[7]])
        else:
            sys.exit(
                color.red_color+"未能获取到符合条件的磁盘!"+color.end_color)

    dir_table.align, disk_table.align = "l", "l"
    disk_table.title = ("磁盘使用率一览表")

    LOGGER.info(f"磁盘使用率一览表.\n{disk_table.get_string(sortby=('序号'))}")
    if if_print_detail == 'yes':
        LOGGER.info(f"目录占用 TOP10 统计完成,见下表.\n{dir_table}")
    _guide()

# 生成 csv 文件
def write_csv(colum_name,tags):
    """_summary_

    Args:
        colum_name (_type_): 表头
        tags (_type_): 分群列表
    """
    with open(csv_file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(colum_name)
        #csv 文件按照占用大小倒叙
        datas=sorted(tags,key=lambda e:e[9],reverse=True)
        writer.writerows(datas)

# 制表统一入口
def table_insert(table_name,table_info):
    """_summary_

    Args:
        table_name (_type_): 表名
        table_info (_type_): 可迭代对象
    """
    for info in table_info:
        table_name.add_row(info)

def _hdfs_list_deal(l:list):
    """_summary_

    Args:
        l (list): 从 hdfs 中获取的占用列表

    Returns:
        tuple: 返回处理之后的列表和大小总和
    """
    if not l:
        return [],0
    cut_list_by_step = [ l[i:i+2] for i in range(0,len(l),2) ]
    sum_size = reduce(lambda x, y: float(x)+float(y),[size[0] for size in cut_list_by_step])
    return cut_list_by_step,sum_size

def _event_statistics ():   
    """_summary_

    Returns:
        _type_: 所有项目所有占用情况,
        格式如：[[['1', 'default', '测试项目', 26.6, 1.5, 0.0], ['1', 'default', '测试项目', [['0', '/sa/data/1/event/18614'], ['0', '/sa/data/1/event/18616']]], [[['0.114941', '/sa/data/1/user_tag/user_tag_pj1_t1_store']]]], [['2', 'production', '正式项目', 2490.7, 252.5, 0.0], ['2', 'production', '正式项目', [['0', '/sa/data/2/event/18621'], ['0', '/sa/data/2/event/18623']]], [[['0', '/sa/data/2/user_tag/user_tag_pj2_t100_store']]]], [['3', 'OKKI_official_site', 'OKKI官网', 3.1, 2.1, 0.0], ['3', 'OKKI_official_site', 'OKKI官网', [['0.00283203', '/sa/data/3/event/18933'], ['0.00283203', '/sa/data/3/event/18934']]], [[['0.135547', '/sa/data/3/user_tag/user_tag_pj3_t307_store']]]]]
    """
    
    project_info_sql = "metadb_cli -usc_dba -D metadata -N -e \"select id,name,cname from sbp_project where name not like '._%' order by id;\""
    project_info_cmd = run_cmd(project_info_sql)['stdout'].strip().split('\n')
    project_info = list(map(lambda info: info.split('\t'), project_info_cmd))
    project_disk = []
    filter_cmd = "awk '{{if ($4 == \"M\")print $3/1024,$NF;else if ($4==\"G\") print $3,$NF;else if ($4==\"T\") print $3*1024,$NF;else print 0,$NF}}'"
    custom_id_cmd = 'aradmin config get global -n customer_id -w literal'
    custom_id = run_cmd(custom_id_cmd)['stdout'].strip()
    for data in project_info:
        try:
            cmd = (f"hdfs dfs -du -s -h /sa/sdw/{custom_id}/data/*/event_ros/data/*|grep merged|{filter_cmd}",
                   f"hdfs dfs -du -s -h /sa/sdw/{custom_id}/data/*/event_ros/data/*|grep -v 'merged'|{filter_cmd}",
                   f"hdfs dfs -du -s -h /sa/sdw/{custom_id}/data/*/sdh_segment*|{filter_cmd}")
            event_total_size_list = run_cmd(cmd[1])['stdout'].strip().split()
            tag_total_size_list = run_cmd(cmd[2])['stdout'].strip().split() if len(run_cmd(cmd[2])['stdout'].strip().split())>0 else [0]
            merge_size_list = run_cmd(cmd[0])['stdout'].strip().split()
            # 分别统计 event,tag,.merge 占用磁盘情况

            event_total_size = _hdfs_list_deal(event_total_size_list)[1]
            tag_total_size = _hdfs_list_deal(tag_total_size_list)[1]
            merge_size = _hdfs_list_deal(merge_size_list)[1]
            
            project_disk.append(
                    [[data[0], data[1], data[2], round(float(event_total_size),1),round(float(tag_total_size),1),round(float(merge_size),1)],
                     [data[0], data[1], data[2],_hdfs_list_deal(event_total_size_list)[0]]])
        except:
            sys.exit(color.red_color +
                     "您所在的环境可能没有 sa 所以无法统计每个项目的 hdfs 占用情况."+color.end_color)
    #[['1', 'default', '测试项目', 0.003453777555555553, 0.6216799599999995, 0, 0], ['2', 'production', '正式项目', 0, 0, 0, 0]]
    return project_disk

def project_used_info():
    """_summary_

    Returns:
        _type_: 表格,表头如（['项目ID', '项目英文名', '项目中文名', '事件占用(G)', '分群占用(G)','merge占用(G)'])）
    """
    cluster_disk_table = prettytable.PrettyTable(
        field_names=['项目ID', '项目英文名', '项目中文名', '事件占用(G)', '分群占用(G)','merge占用(G)'])
    cluster_disk_table.align = 'l'
    table_insert(cluster_disk_table,[i[0] for i in _event_statistics()])
    return cluster_disk_table

def count_event_dfs(event_list_by_time):
    """_summary_

    Args:
        event_list_by_time (_type_): 按照时间过滤好的 event 数组

    Returns:
        _type_: 事件之和
    """
    if not event_list_by_time:
        return 0.0
    return (reduce(lambda x, y: round(float(x)+float(y),2),[ info[0] for info in event_list_by_time ]))

@log('get_tag_disk')
def _get_tag_disk():
    colum_name_list=['分群/标签英文名称', '分群/标签中文名称', '创建时间', '编辑时间', '分群类型', '用户英文名', '用户中文名', '项目英文名', '项目中文名', '占用(G)']
    offline_table_normal = prettytable.PrettyTable(field_names=colum_name_list)
    online_table_normal = prettytable.PrettyTable(field_names=colum_name_list)
    not_clean_table = prettytable.PrettyTable(
        field_names=['未释放的分群/标签路径', '占用(G)'])
    csv_data=[]

    idcmd = "sa_mysql -D metadata -N -e \"select distinct(pj.id) from project pj join sp_user_tag sut on pj.id=sut.project_id where pj.name not like '._%' order by pj.id;\""
    tag_count_cmd = "sa_mysql -D metadata -N -e \"select count(*) from sp_user_tag;\""
    all_tag_count = run_cmd(tag_count_cmd)['stdout'].replace('\n', ',').split(',')
    all_tag_size_list = []
    project_list = run_cmd(idcmd)['stdout'].strip().replace('\n', ',').split(',')
    if len(''.join(project_list)) == 0:
        sys.exit(color.red_color +
                 "未能获取到分群信息,请确认当前环境是否存在分群或者标签."+color.end_color)
    for projectId in project_list:
        tag_size_cmd = f"hdfs dfs -du -s -h /sa/data/{projectId}/user_tag/*|awk '{{if ($4 == \"M\")print $3/1024;else if ($4==\"G\") print $3;else if ($4==\"T\") print $3*1024;else print 0}}'"
        tag_size = run_cmd(tag_size_cmd)['stdout'].strip().split('\n')
        all_tag_size_list.append(tag_size)
        tagcmd = f"hdfs dfs -du -s -h /sa/data/{projectId}/user_tag/* | egrep 'G|T' | wc -l"
        tagnum = run_cmd(tagcmd)['stdout'].strip()
        if int(tagnum) > 0:
            hdfsinfocmd = f"hdfs dfs -du -s -h /sa/data/{projectId}/user_tag/*|egrep 'G|T' | grep '_store'" + \
                "|awk '{if ($4==\"G\") print $3,$5;else if ($4==\"T\") print $3*1024,$5}'"
            hdfsinfo_tmp=[data.split(' ') for data in run_cmd(hdfsinfocmd)['stdout'].strip().split('\n')]
            hdfsinfo=[[float(data[0]),data[1]] for data in hdfsinfo_tmp]
            tag=str([data[1].split('_')[4].strip('t') for data in hdfsinfo]).replace('[','(').replace(']',')').replace('\'','')
            tagcmd = f"sa_mysql -D metadata -N -e \"select t.id,t.name as fqname,t.cname as fqcname,date_format(t.create_time,'%Y-%m-%d %H:%i:%s') as createtime,\
                    date_format(t.update_time,'%Y-%m-%d %H:%i:%s') as updatetime,(case when t.is_routine =0 then '手动' when t.is_routine =1 then '例行' else '其他' end) as fqlx,u.username as username,u.user_cname as usercname,\
                    pj.name as pjname,pj.cname as pjcname from sp_user_tag t,user u,project pj where t.user_id=u.id and pj.id=t.project_id and t.id in {tag}\""
            db_taginfos_list=[data.split('|||||') for data in '|||||'.join(run_cmd(tagcmd)['stdout'].strip().split('\t')).split('\n')]
            if len(db_taginfos_list[0][0])>0:
                online_tag_info=[data for data in db_taginfos_list if  data[1].count('plan_pl') >0 ] 
                offline_tag_info=[data for data in db_taginfos_list if data[1].count('plan_pl') ==0]
                offline_tag_success=[data for data in hdfsinfo if data[1].split('_')[4].strip('t') in [ tag[0] for tag in offline_tag_info ]]
                online_tag_success=[data for data in hdfsinfo if data[1].split('_')[4].strip('t') in [ tag[0] for tag in online_tag_info]]
                tag_falid=[data[::-1] for data in hdfsinfo if data[1].split('_')[4].strip('t') not in [ tag[0] for tag in offline_tag_info+online_tag_info]]

                #将 db 中分群/标签信息和 hdfs 信息一一对应融合
                offline_tag_info_dic={}
                online_tag_info_dic={}
                for info in offline_tag_info:
                    offline_tag_info_dic.update({info[0]:info[1:11]})
                for info in online_tag_info:
                    online_tag_info_dic.update({info[0]:info[1:11]})
                offline_suminfo=[offline_tag_info_dic.get(info[1].split('_')[4].strip('t'))+[info[0]] for info in offline_tag_success]
                online_suminfo=[online_tag_info_dic.get(info[1].split('_')[4].strip('t'))+[info[0]] for info in online_tag_success]
                table_insert(offline_table_normal,offline_suminfo)
                table_insert(online_table_normal,online_suminfo)
                csv_data+=offline_suminfo+online_suminfo
                table_insert(not_clean_table,tag_falid)
            else:
                #not_clean_table.add_rows(data[::-1] for data in hdfsinfo)
                table_insert(not_clean_table,(data[::-1] for data in hdfsinfo))
    all_tag_size = reduce(lambda x,y:float(x)+float(y),reduce(lambda x,y:x+y,[i for i in all_tag_size_list if len(i)>1]))
    offline_table_normal.align,online_table_normal.align,not_clean_table.align='l','l','l'
    if len(csv_data) > 0:
        write_csv(colum_name_list, csv_data)
        all_project_tag_sum = reduce(
            lambda x, y: round(x+y, 2), list(zip(*csv_data))[9])
    else:
        all_project_tag_sum = 0
    offline_table_normal.title = (f"当前环境分群/标签共 {all_tag_count[0]} 个,占用 {round(all_tag_size,2)}G,其中较大的分群/标签有 {len(csv_data)} 个,占用 {all_project_tag_sum}G.")
    LOGGER.info(f"计算完成,若有大分群/标签,可以引导客户适当清理一些不用的或者缩短保留时间,以释放一定的空间!\n{offline_table_normal.get_string(sortby='占用(G)',reversesort=True)}\n以下为在线产品(sf)产生的分群\n{online_table_normal.get_string(sortby='占用(G)',reversesort=True)}")
    LOGGER.info(color.yellow_color +
                f"以下表格若有数据说明是 web 前端删了分群或标签但是占用 hdfs 的存储还未释放，其中 user_group_xxx 为用户分群次日会自动清理，user_tag_xxx 为用户标签默认30天后会自动清理!\n{not_clean_table}"+color.end_color)
    print(color.green_color+"若需要分群文件,请自行下载 /home/sa_cluster/tag.csv"+color.end_color)

# 分群运行情况


@log('get_user_tag_info')
def _get_user_tag_info(begintime, endtime):
    """
    获取分群或者标签运行情况
    :param begintime:  # 开始时间
    :param endtime:  # 结束时间
    """
    date_reg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reg_check = re.compile('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    table_name = ['sp_user_tag', 'sp_user_tag_partition',
                  'sps_partition_task', 'sps_user_group']
    for table in table_name:
        table_if_exist = subprocess.check_output(
            f"sa_mysql -D metadata -N -e \"show tables like '{table}';\"|wc -l", shell=True, universal_newlines=True).strip()
        if int(table_if_exist) == 0:
            sys.exit(color.red_color +
                     f"[ {table} not exist,plese check sps version! ]"+color.end_color)
    if not (reg_check.match(begintime) and reg_check.match(endtime)):
        sys.exit(color.red_color +
                 f"[ please input valid date,like {date_reg}! ]"+color.end_color)
    success_fail_waitting_list = []
    failed_waitting_list = []
    table_success = prettytable.PrettyTable(field_names=[
        '分群/标签ID', '分群/标签英文名称', '分群/标签中文名称', '类型', '项目英文名', '项目中文名', '开始时间', '结束时间', '耗时', '运行状态'])
    table_fail = prettytable.PrettyTable(field_names=[
        '分群/标签ID', '分群/标签英文名称', '分群/标签中文名称', '类型', '项目英文名', '项目中文名', '时间', '运行状态', '原因'])
    tag_run_info_sql = f"sa_mysql -D metadata -N -e \"select A.id,A.name,A.cname,A.fqlx,A.bname,A.bcname,B.begintime,B.endtime,timestampdiff(SECOND,B.begintime,B.endtime) as elapse,B.status from (select a.name as name,a.cname as cname,b.name as bname ,b.cname as bcname ,a.id,(case when a.is_routine =0 then '手动' when a.is_routine =1 then '例行' else '其他' end) as fqlx from sp_user_tag a join project b on a.project_id=b.id  where a.project_id=b.id) A left join (select a.id,b.id as bid,a.name,b.user_tag_id,b.start_time as begintime,b.finished_time as endtime,b.status as status from sp_user_tag as a left join sp_user_tag_partition as b on a.id = b.user_tag_id where  b.start_time < '{endtime}' and b.start_time > '{begintime}') B on A.id=B.user_tag_id where A.name=B.name order by A.id;\""
    sql_result = re.split('\t|\n', run_cmd(tag_run_info_sql)['stdout'].strip())
    if len(sql_result) == 1:
        sys.exit(color.red_color +
                 "未能获取到分群信息!\n1、当前环境是否存在分群或者标签？\n2、程序执行时日期参数填写是否合理？"+color.end_color)

    for i in range(0, len(sql_result), 10):
        success_fail_waitting_list.append(sql_result[i:i+10])

    for result in success_fail_waitting_list:
        if result[9] == 'SUCCEED':
            table_success.add_row([result[0], result[1], result[2], result[3],
                                   result[4], result[5], result[6], result[7], result[8], result[9]])
        else:
            failed_waitting_list.append(result)

    for fw_result in failed_waitting_list:
        fw_result_sql = f"sa_mysql -D metadata -N -e \"select spt.refer_key,spt.refer_type,spt.start_time,spt.fail_message,sug.status from sps_partition_task as spt,sps_user_group as sug where sug.name=spt.refer_key and spt.refer_key='{fw_result[1]}' and sug.tag_id={fw_result[0]} and spt.start_time like '{fw_result[6][0:10]}%';\""
        fw_result_sql_result = re.split(
            '\t|\n', run_cmd(fw_result_sql)['stdout'].strip())

        for m in range(0, len(fw_result_sql_result), 5):
            if len(fw_result_sql_result) > 1:
                if len(fw_result_sql_result[m:m+5][3]) > 0:
                    fw_result.append(fw_result_sql_result[m:m+5][3])
                    table_fail.add_row([fw_result[0], fw_result[1], fw_result[2], fw_result[3],
                                        fw_result[4], fw_result[5], fw_result[6], fw_result[8], fw_result[9]])
    table_success.align, table_fail.align = "l", "l"
    LOGGER.info(f"计算成功的分群如下表:\n{table_success}")
    LOGGER.info(color.yellow_color +
                f"计算失败的分群如下表:\n{table_fail}"+color.end_color)


# 获取hdfs中各个目录大小，目录深度为2
result = []
hdfs_cmd = "sudo -u hdfs hdfs dfs -du -s -h" if len((run_cmd(
    "grep hdfs /etc/passwd|awk -F: '{print $1}'")['stdout'].split())) == 1 else "hdfs dfs -du -s -h"


def hdfs_du_info(d='/'):
    ls_cmd_info = f"hdfs dfs -ls {d}" + \
        "|grep -v system|awk '/^d/'|awk '{print $(NF-7),$NF}'"
    dirs = run_cmd(ls_cmd_info)['stdout'].split()
    #['drwxrwxrwt', '/app-log', 'drwxr-xr-x', '/ats', 'drwxr-xr-x', '/mapred', 'drwxrwxrwx', '/mr-history', 'drwxr-xr-x', '/sa', 'drwxr-xr-x', '/sdp', 'drwxrwxrwx', '/tmp', 'drwxr-xr-x', '/user']
    for i in range(0, len(dirs), 2):
        if dirs[i:i+2][1].count('/') >= 3:
            continue
        tmp = run_cmd(
            f"{hdfs_cmd} {dirs[i:i+2][1]}|egrep -w 'G|T'|head -8")['stdout'].split()
        res = [data for data in tmp if float(tmp[0]) != 0 and len(tmp) != 0]
        if len(res) > 0 and dirs[i:i+2][0].startswith('d'):
            hdfs_du_info(res[4])
            result.append(res)


def _get_hdfs_du_info():
    hdfs_disk_table = prettytable.PrettyTable(field_names=['HDFS 目录', '大小(G)','副本数'])
    hdfs_disk_table.title = ("HDFS 占用一览表")
    hdfs_disk_table.align = 'l'
    hdfs_du_info()
    for i in result:
        if i[1] == 'T':
            i[0], i[1] = round(float(i[0])*1024, 1), 'G'
        if i[3] == 'T':
            i[2], i[3] = round(float(i[2])*1024, 1), 'G'
        hdfs_replical_info = 'normal' if (float(i[2])/float(i[0]))<5 else f'{color.red_color}abnormal{color.end_color}{color.green_color}'
        hdfs_disk_table.add_row([i[4], i[2],hdfs_replical_info])
    return hdfs_disk_table.get_string(sortby='HDFS 目录')



@log('get_event_size_by_time')
def _get_event_size_by_time(start ,end):
    """_summary_

    Args:
        start (_type_): hdfs 中的开始时间
        end (_type_): hdfs 中的结束时间
    """
    defaulteTime = (datetime.datetime.now()).strftime("%Y-%m-%d")
    if not (_time_trans(start) and _time_trans(end)):
        sys.exit(color.red_color +
                  f"[ please input valid date,like ['{defaulteTime}']! ]"+color.end_color)
    filter_list = []
    event_disk_table = prettytable.PrettyTable(
        field_names=['项目ID', '项目英文名', '项目中文名', '近 6 个月(G)', '近 12 个月(G)',f'{start} 至 {end}(G)'])
    event_disk_table.align = 'l'
    
    # 获取指定日期范围的事件占用 hdfs 的情况
    
    for i in _event_statistics():

        event_list_by_time = [ e for e in i[1][3] if _time_trans(start) <= int(e[-1].split('/')[-1]) <=_time_trans(end) ]
        event_list_60_days = [ e for e in i[1][3] if _time_trans(defaulteTime)- 180 <= int(e[-1].split('/')[-1]) <=_time_trans(defaulteTime) ]
        event_list_120_days = [ e for e in i[1][3] if _time_trans(defaulteTime)- 365 <= int(e[-1].split('/')[-1]) <=_time_trans(defaulteTime) ]

        filter_list.append([i[1][0],i[1][1],i[1][2],count_event_dfs(event_list_60_days),count_event_dfs(event_list_120_days),count_event_dfs(event_list_by_time)])
    table_insert(event_disk_table,filter_list)
    event_disk_table.title = ("事件占用磁盘一览表")
    LOGGER.info(f"事件占用磁盘情况获取完成,见下表.\n{event_disk_table}")
    

# 获取各个节点磁盘增长情况
def _get_disk_increase():
    """_summary_

    Returns:
        _type_: 磁盘占用情况
    [(('/sensorsdata/rnddata00', [1689071992.573, '498808733696']), ('/sensorsdata/rnddata00', [1689071992.643, '497926877184']), ('/sensorsdata/rnddata00', [1689071992.691, '549487378432'])), (('/sensorsdata/seqdata00', [1689071992.573, '498808733696']), ('/sensorsdata/seqdata00', [1689071992.643, '497926877184']), ('/sensorsdata/seqdata00', [1689071992.691, '549487378432'])), (('/sensorsdata/stdata', [1689071992.573, '498808733696']), ('/sensorsdata/stdata', [1689071992.643, '497926877184']), ('/sensorsdata/stdata', [1689071992.691, '549487378432'])), (('/sensorsmounts/hybriddata', [1689071992.573, '498808733696']), ('/sensorsmounts/hybriddata', [1689071992.643, '497926877184']), ('/sensorsmounts/hybriddata', [1689071992.691, '549487378432'])), (('/sensorsdata/main', [1689071992.573, '253570838528']), ('/sensorsdata/main', [1689071992.643, '250115932160']), ('/sensorsdata/main', [1689071992.691, '429287014400'])), (('/sensorsdata/metadata', [1689071992.573, '253570838528']), ('/sensorsdata/metadata', [1689071992.643, '250115932160']), ('/sensorsdata/metadata', [1689071992.691, '429287014400'])), (('/sensorsmounts/metadata', [1689071992.573, '253570838528']), ('/sensorsmounts/metadata', [1689071992.643, '250115932160']), ('/sensorsmounts/metadata', [1689071992.691, '429287014400']))]
    """

    metricDefine = namedtuple(
        'promQlDefine', ['totaldisk', 'freedisk', 'job', 'mountpoint'])
    metric = metricDefine('node_filesystem_size_bytes',
                          'node_filesystem_free_bytes', 'sensors-inf-component', '.data.*|.sensorsmounts.*|.kudu.*|.kafka.*')
    promQl = f'{{job="{metric.job}",mountpoint=~".*{metric.mountpoint}.*"}}'
    prometheus_host = DeployTopo().get_host_list_by_module_name(
        'sm', 'prometheus')[0]
    disk_urls = (f'http://{prometheus_host}:8310/api/v1/query?query=max_over_time({metric.freedisk}{promQl}[10d])',
                 f'http://{prometheus_host}:8310/api/v1/query?query={metric.freedisk}{promQl}',
                 f'http://{prometheus_host}:8310/api/v1/query?query={metric.totaldisk}{promQl}')
    response = {
        'disk_before_free': requests.get(url=disk_urls[0]),
        'disk_now_free': requests.get(url=disk_urls[1]),
        'total_disk': requests.get(url=disk_urls[2])
    }
    results = {}
    for k, v in response.items():
        if v:
            tmp = (list(zip(([data['metric']['mountpoint'] for data in json.loads(v.content.decode())['data']['result']]),
                            [data['value'] for data in json.loads(v.content.decode())['data']['result']])))
            results[k] = tmp
    return results

# 单机扩容


def _simple_disk_evaluate(dn):
    """_summary_

    Args:
        dn (_type_): disk_name
    """    
    
    simple_suggest_list = []
    if type(dn) is list:
       dn = dn[0]
       local_df_info =  f"df -Th|grep -E {dn}" + \
        "|awk '{print $(NF-6),$(NF-5),$(NF-4),$(NF-3),$(NF-2),$(NF-1),$(NF)}'|awk  '{if($1 != \"Type\") print($7)}'"
    else:
       local_df_info = f"df -Th|grep -v tmpfs" + \
        "|awk '{print $(NF-6),$(NF-5),$(NF-4),$(NF-3),$(NF-2),$(NF-1),$(NF)}'|awk  '{if($1 != \"Type\" && $6 > \"75%\") print($7)}'"
    disk_names = run_cmd(local_df_info)['stdout'].strip().split()
    if not disk_names:
        sys.exit(color.yellow_color +
                "未找到符合规则的磁盘:\n1:磁盘使用率未超过 80%.\n2:磁盘名称不存在."+color.end_color)
    dir_reg = '|'.join(disk_names)
    all_disk_info = list(zip(_get_disk_increase().get('disk_before_free'), _get_disk_increase().get('disk_now_free'), _get_disk_increase().get('total_disk')))
    # {'disk_name':['disk_used','now_disk','total']}
    current_disk_info = {disk_info[0][0]:[(int(disk_info[0][1][1])-int(disk_info[1][1][1]))/1024**3,int(disk_info[1][1][1]),int(disk_info[2][1][1])] for disk_info in all_disk_info if disk_info[0][0] in disk_names }
    for k,v in current_disk_info.items():
        disk_used_rate_by_day = v[0]/10
        expected_for_use = 30*12*round(v[0]/10)
        current_available = (0.9*v[1]/1024**3)/disk_used_rate_by_day
        simple_suggest_list.append(
                    f"# 现状:当前环境 {k} 盘,共 {round(v[2]/1024**3,1)}G,使用率较高,详情见下述「磁盘使用率一览表」.\n# 方案:\n    ➤ 按照当前每天 {round(disk_used_rate_by_day,2)}G 的增长情况估算,若将 {k} 扩 {expected_for_use}G,预计可使用 12 个月,磁盘剩余 {round(v[1]/1024**3)}G,距离到达 90% 预计还可使用 {round(current_available)} 天.\n")
    simple_suggest_list_to_str = ''.join(simple_suggest_list)
    if len(simple_suggest_list) > 0:
        suggestions = f"""
========================================磁盘扩容需积极========================================

{simple_suggest_list_to_str}

========================================故障丢数不可取========================================

"""
        LOGGER.info("正在获取 hdfs 中各个目录的使用情况,请稍后...")
        LOGGER.info(f"下述「HDFS 占用一览表」需关注如下情况\n1:若非[/sa/data]目录较大,需要具体确认子目录使用情况,如果用不到可以删除释放部分存储\n2:副本数一列若出现[abnormal]请反馈给到「AIOP 工单整治」群\n{_get_hdfs_du_info()}")
        LOGGER.info(f"现状及扩容方案如下.\n{suggestions}")
    else:
        LOGGER.info("很棒,当前环境的磁盘无需扩容!")
    _get_disk_info([0], 'yes', [dir_reg])

# 获取集群环境磁盘扩容方案

def _cluster_disk_evaluate():
    suggestions_table = prettytable.PrettyTable(
        field_names=['方案', '内容'])
    suggestions_table.align = 'l'
    storage_dirs_info = InnerDirectoryInfo().get_all_storage_dir()
    seq_dir = {k: v['storage_dirs_info']['sequence']['storage_dir_path']
               for k, v in storage_dirs_info.items() if (v['storage_dirs_info'].get('sequence') is not None)}  # v['node_type'] == 'data' or v['node_type'] == 'hybrid'
    dir_reg_tmp = ['|'.join(data).replace('/sa_cluster', '')
                   for data in seq_dir.values()]
    all_seqdata = []
    for i in [data.split('|') for data in dir_reg_tmp]:
        [all_seqdata.append(data) for data in i]
    dir_reg = '|'.join(all_seqdata).replace(
        'sensorsdata', 'sensorsmounts')+'|/sensorsmounts/seqdata|/sensorsdata/seqdata'
    disk_dic = {
        'all_seqdata_before_free_bytes': 'disk_before_free',
        'all_seqdata_now_free_bytes': 'disk_now_free',
        'all_seqdata_bytes': 'total_disk'
    }
    try:

        seq_disk_dic = {k: [data[1][1] for data in _get_disk_increase().get(
            v) if data[0] in [data2 for data2 in all_seqdata]] for k, v in disk_dic.items()}
        disk_count = len(all_seqdata)
        each_seqdata = round(
            int(seq_disk_dic.get('all_seqdata_bytes')[0])/1024**3)
    except:
        sys.exit(color.red_color +
                 "该环境应该是个老环境且存在磁盘挂载非标现象,辛苦人工大概评估吧,拜拜喽!"+color.end_color)
    total_disk_used_by_day = round((reduce(lambda x, y: int(x)+int(y), seq_disk_dic.get('all_seqdata_before_free_bytes')) -
                                    reduce(lambda x, y: int(x)+int(y), seq_disk_dic.get('all_seqdata_now_free_bytes')))/1024**3/25, 2)
    if_archive = "当前环境存在归档" if (run_cmd(
        'sdfadmin archive status 2>&1|grep enable|wc -l')['stdout'].split()[0]) == '1' else "当前环境没有归档"

    suggest_str = None
    if each_seqdata < 1024*4:
        suggest_str = f"基于当前的增长情况,下述「磁盘使用率一览表」中,若每块顺序盘扩 500G,预计可使用 {round(500*disk_count/(total_disk_used_by_day*30),1)} 个月;若每块顺序盘扩 1000G,预计可使用 {round(1000*disk_count/(total_disk_used_by_day*30),1)} 个月."
    else:
        suggest_str = f"基于当前的增长情况,下述「磁盘使用率一览表」中各节点若各加 1 块 {each_seqdata}G 顺序盘,预计可使用 {round(each_seqdata*len(dir_reg_tmp)/(total_disk_used_by_day*30),1)} 个月;若各加 2 块 {each_seqdata}G 顺序盘,按照当前近期使用情况,预计可使用 {round(2*each_seqdata*len(dir_reg_tmp)/(total_disk_used_by_day*30),1)} 个月."
    suggestions_list=[
        ['删历史数据','可以参考神策官网「https://manual.sensorsdata.cn/sa/latest/sdfadmin-107905989.html」清理历史数据释放存储.'],
        ['扩容数据盘',f'{suggest_str}'],
        ['做数据归档','若无归档且磁盘 >=2T,也可以考虑开启归档进行磁盘释放,仅集群环境支持归档,此操作由 TAM 提「归档」类型的 SOR 工单由神策运维同学开启.']
    ]
    suggestions_table.title=f"现状:当前环境共有 {disk_count} 块顺序盘,每块顺序盘 {each_seqdata}G,共 {each_seqdata*disk_count}G,每天增长 {total_disk_used_by_day}G,磁盘使用率较高,需参考如下方案进行处理."
    table_insert(suggestions_table,suggestions_list)
    suggestions = f"""
================================================磁盘扩容需积极================================================
{suggestions_table}
================================================故障丢数不可取================================================
"""
    LOGGER.info(if_archive)
    LOGGER.info("正在获取 hdfs 中各个目录的使用情况,请稍后...")
    LOGGER.info(f"下述「HDFS 占用一览表」需关注如下情况\n1:若非[/sa/data]目录较大,需要具体确认子目录使用情况,如果用不到可以删除释放部分存储\n2:副本数一列若出现 abnormal 请反馈给到「AIOP 工单整治」群\n{_get_hdfs_du_info()}")
    LOGGER.info(f"当前环境磁盘使用情况使用情况.\n{project_used_info()}")
    LOGGER.info(
                f"注意:\n1、若有大分群可以引导客户清理或者缩短保留时间.\n2、merge 如果很大,比如超过1T,可以找导入接口人确认.\n3、hdfs 中若非 /sa/data 目录较大,需要具体确认具体占用内容.\n4、确认下述「磁盘使用率一览表」中的磁盘是否存在异构现象,如果异构需要统一大小.\nPS:上述情况都没有则可以将下面的扩容方案转附到工单并将工单转给 tam.\n{suggestions}")
    _get_disk_info([0], 'no', [dir_reg])



def _disk_evaluate(disk_name):
    if len(_get_ssh_info()[1]) == 1:
        LOGGER.info(f"当前是单机环境,正在获取磁盘使用情况及扩容方案,请稍后...")
        _simple_disk_evaluate(disk_name)
    elif len(_get_ssh_info()[1]) == 3:
        LOGGER.info("当前是 3 节点迷你集群,正在获取磁盘使用情况及扩容方案,请稍后...")
        _cluster_disk_evaluate()
    else:
        LOGGER.info(f"当前是 3+{len(_get_ssh_info()[1])-3} 集群,正在获取磁盘使用情况及扩容方案,请稍后...")
        _cluster_disk_evaluate()



def _areparse():
    parser = argparse.ArgumentParser(
        description=f"{color.green_color}用于分析 AIOP 磁盘使用情况,没有任何修改或删除的操作!{color.end_color}")
    parser.add_argument('-r', '--disk-rate', nargs=1, type=int, default=[0], action='store',
                        help=f'获取各个节点磁盘使用率.\n例子:[ python3 {os.path.basename(__file__)} -r 30 ]')
    parser.add_argument('-p', '--print-detail', default='no', action='store',
                        choices=['yes', 'no'], help=f'是否打印目录占用明细TOP10,不可单独使用,建议与参数[-r,-n]配合使用.\n例子:[ python3 {os.path.basename(__file__)} -r 30 -p yes ]')
    # parser.add_argument('-c', '--customer-info',
    #                     action='store_true', help=f'获取部署信息,单独使用.(未来会弃用!)\n例子:[ python3 {os.path.basename(__file__)} -c ]')
    parser.add_argument('-n', '--disk-name', nargs=1,
                        type=str, default=' ', action='store', help=f'根据磁盘名称获取磁盘使用情况,模糊匹配,支持正则,可与参数[ -r,-p ]配合使用.\n例子:[ python3 {os.path.basename(__file__)} -n metadata -p no ]')
    parser.add_argument('-t', '--get-user-tag-info', nargs=2,
                        help=f"显示分群执行情况. \n例子: [ python3 {os.path.basename(__file__)} -t '2022-07-06 00:00:00' '2022-07-06 10:00:00' ]")
    parser.add_argument('-d', '--get-tag-disk', action='store_true',
                        help=f"显示分群占用 hdfs 大小. \n例子: [ python3 {os.path.basename(__file__)} -d ]")
    parser.add_argument('-e', '--evaluate', action='store_true',
                        help=f"评估方案获取,可将此结果贴图至工单评论区并告知对应 tam. \n例子: [ python3 {os.path.basename(__file__)} -e|-en<diskname> ]")
    parser.add_argument('-dfs', '--event-growth',nargs=2,
                        help=f"获取指定时间段 event 占用磁盘情况,时间区间为闭区间. \n例子: [ python3 {os.path.basename(__file__)} -dfs '2022-07-06' '2022-07-28' ]")

    return parser.parse_args()


def main():
    LOGGER.info(f'工具版本号:{VERSION}')
    if (getpass.getuser()) != 'sa_cluster':
        sys.exit("please use sa_cluster account.")
    parser = _areparse()
    arg_list_disk = ['-r', '-p', '-n', '-c']
    if (arg_list_disk[0] in sys.argv or arg_list_disk[1] in sys.argv or arg_list_disk[2] in sys.argv) and sys.argv[1] != "-p":
        _get_disk_info(parser.disk_rate, parser.print_detail, parser.disk_name)
    # elif arg_list_disk[3] in sys.argv:
    #     _get_customer_info()
    elif parser.get_user_tag_info:
        _get_user_tag_info(
            parser.get_user_tag_info[0], parser.get_user_tag_info[1])
    elif parser.get_tag_disk:
        _get_tag_disk()
    elif parser.evaluate:
        _disk_evaluate(parser.disk_name)
    elif parser.event_growth:
        _get_event_size_by_time(parser.event_growth[0],parser.event_growth[1])
    else:
        sys.exit(
            color.red_color+f"please input one valid argument at least,You can get help through [ python3 {os.path.basename(__file__)} -h ]"+color.end_color)
    print(color.yellow_color +
          f"日志详见: [ less {FILE_NAME} ]"+color.end_color)


if __name__ == '__main__':
    main()
