'''
create_time: 2023/8/24 10:11
author: yss
version: 1.0
desc: 排查数据源接入的报错
'''

import os
import pymysql
import argparse
import paramiko
from hyperion_client.hyperion_inner_client.inner_config_manager import InnerConfigManager


def analysis_datasource(d_table,d_type):
    # 获取连接信息
    mysql_host = InnerConfigManager.get_instance().get_mysql_master()
    mysql_pass = InnerConfigManager.get_instance().get_client_conf('sp', 'mysql')['password']
    # 打开数据库连接
    db = pymysql.connect(host=mysql_host,user='work',password=mysql_pass,database='metadata',port=3305)

    # 获取游标对象
    cursor = db.cursor()

    # 获取 job_id
    sql = "select id from sdg_ingestion_job where name like '%{}%' and type='{}' and delete_flag=0".format(d_table,d_type)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        job_id = data[0]
    else:
        print('{} 没有错误信息.'.format(d_table))
        exit(0)


    # 获取错误信息
    sql = "select execution_result from sdg_ingestion_job_handle where job_id={} and status='failure' order by start_time desc limit 1;".format(job_id)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        failed_reason = data[0]
    else:
        print('{} 没有错误信息.'.format(d_table))
        exit(0)

    # 打印粗略的失败原因
    print('{} 错误信息: {}'.format(d_table,failed_reason))

    # 获取job_handle_id
    sql = "select id from sdg_ingestion_job_handle where job_id={} and status='failure' order by start_time desc limit 1;".format(job_id)
    cursor.execute(sql)
    job_handle_id = cursor.fetchone()[0]

    # 打印错误步骤的信息
    sql = "select message from sdg_ingestion_job_handle_process where job_handle_id={} order by create_time desc limit 1;".format(job_handle_id)
    cursor.execute(sql)
    detail_failed_reason = cursor.fetchone()[0]
    print('{} 较为详细的错误信息： {}'.format(d_table,detail_failed_reason))

    sql = "select schedule_instance from sdg_ingestion_job_handle where job_id={} and status='failure' order by start_time desc limit 1;".format(job_id)
    cursor.execute(sql)
    execute_host = cursor.fetchone()[0].split('.')[0]

    log_name ='{}-jobId-{}-jobHandleId-{}.log'.format(d_type,job_id,job_handle_id)
    path1 = os.path.join(os.environ['SENSORS_DATA_GOVERNOR_LOG_DIR'],'ingestion_flink_job',log_name)
    path2 = os.path.join(os.environ['SENSORS_DATA_GOVERNOR_LOG_DIR'],'web',log_name)

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    ssh_client.connect(hostname=execute_host)
    cmd = 'test -e {} && grep ERR -A 10 -m 3 {}'.format(path1,path1)
    stdin,stdout,stderr = ssh_client.exec_command(cmd)
    print('{} 详细的错误信息：{}'.format(d_table,stdout.read().decode('utf-8')))

    cmd = 'test -e {} && grep ERR -A 10 -m 3 {}'.format(path2,path2)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print('{} 详细的错误信息：{}'.format(d_table, stdout.read().decode('utf-8')))

    ssh_client.close()
    db.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='analysis_datasource question')
    parser.add_argument('table',help='datasource table name')
    parser.add_argument('type',help='dataSync or dataPublish')
    args = parser.parse_args()


    analysis_datasource(args.table,args.type)
