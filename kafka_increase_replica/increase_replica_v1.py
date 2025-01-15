'''
create_time: 2024/1/29 10:55
author: yss
version: 1.0
'''
import argparse
import os
import subprocess
import sys

from kazoo.client import KazooClient
import json
import random

RUNTIME_DIR = '/tmp/increase_replica'


def get_kafka_broker_id(zookeeper_host):
    # 创建Kazoo客户端
    zk = KazooClient(hosts=zookeeper_host)

    # 连接到ZooKeeper服务器
    zk.start()

    # 获取Kafka的Broker ID
    broker_id_list = None

    try:
        broker_id_list = zk.get_children("/brokers/ids")
    except Exception as e:
        print(f"Error: {e}")

    # 关闭ZooKeeper连接
    zk.stop()
    return broker_id_list  # 返回值是 list


def increase_partition(topic_name,zookeeper_host):
    os.makedirs(RUNTIME_DIR,exist_ok=True) # 创建工作目录
    os.chdir(RUNTIME_DIR)

    reassign_script = '/data/sa_cluster/cloudera/parcels/KAFKA-4.1.0-1.4.1.0.p0.4/lib/kafka/bin/kafka-reassign-partitions.sh'
    if os.path.exists('/data/sa_cluster/cloudera/parcels/KAFKA-4.1.0-1.4.1.0.p0.4/lib/kafka/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/data/sa_cluster/cloudera/parcels/KAFKA-4.1.0-1.4.1.0.p0.4/lib/kafka/bin/kafka-reassign-partitions.sh'
    elif os.path.exists('/sensorsdata/main/program/sp/sdp/1.0.0.0-123/kafka/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/sensorsdata/main/program/sp/sdp/1.0.0.0-123/kafka/bin/kafka-reassign-partitions.sh'
    elif os.path.exists('/sensorsdata/main/program_entity/kafka/artifacts/kafka_core/2.8.1.3094/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/sensorsdata/main/program_entity/kafka/artifacts/kafka_core/2.8.1.3094/bin/kafka-reassign-partitions.sh'
    elif os.path.exists('/sensorsdata/main/program_entity/kafka/artifacts/kafka_core/2.8.2.3225/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/sensorsdata/main/program_entity/kafka/artifacts/kafka_core/2.8.2.3225/bin/kafka-reassign-partitions.sh'
    elif os.path.exists('/sensorsdata/main/program/kafka/kafka/kafka_broker/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/sensorsdata/main/program/kafka/kafka/kafka_broker/bin/kafka-reassign-partitions.sh'

    if not os.path.exists(reassign_script):
        print('kafka-reassign-partitions.sh 脚本路径找不到，不能使用此脚本')
        exit(1)

    topic_json = '{"topics": [{"topic": "%s"}],"version": 1}' % topic_name  # 格式化字符串

    reassign_file = os.path.join(RUNTIME_DIR,'{}.json'.format(topic_name))

    with open(reassign_file,'w') as f:  # 创建文件写入 json 数据
        f.write(topic_json)

    broker_id_list = get_kafka_broker_id(zookeeper_host)
    broker_id_list_str = ','.join(broker_id_list)

    reassign_cmd = f'{reassign_script} --zookeeper {zookeeper_host} --topics-to-move-json-file {reassign_file} ' \
                   f'--broker-list {broker_id_list_str}  --generate |grep Current -A 1|grep -v Current'

    try:
        completed_process = subprocess.run(reassign_cmd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = completed_process.stdout
    except Exception as e:
        print(f"执行命令时出错: {str(e)}")

    output_obj = json.loads(output) # json 字符串转成 python 对象

    for partition in output_obj['partitions']:
        replica_list = partition['replicas']
        tmp_replica_list = broker_id_list[:]  # 复制列表

        for i in replica_list:
            tmp_replica_list.remove(str(i))
        else:
            choice_id = random.choice(tmp_replica_list)
            replica_list.append(int(choice_id))  # 增加 broker id

        log_dir = partition['log_dirs'][0]
        partition['log_dirs'].append(log_dir)  # 增加 log_dir

    # 目前已经获取到了当前的 topic partition 信息，以下编写新的增加副本信息
    reassign_increase_file = os.path.join(RUNTIME_DIR,'{}_increase.json'.format(topic_name))

    with open(reassign_increase_file,'w') as file:   # 获取到的结果输出到文件中
        file.write(json.dumps(output_obj))

    reassign_cmd_exec = f'{reassign_script} --zookeeper {zookeeper_host} --reassignment-json-file {reassign_increase_file} --execute|sed -n "3p"'

    try:
        completed_process = subprocess.run(reassign_cmd_exec, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = completed_process.stdout
    except Exception as e:
        print(f"执行命令时出错: {str(e)}")

    print('{} 扩副本完成，使用如下命令检查扩容结果：'.format(topic_name))
    print(f'{reassign_script} --zookeeper {zookeeper_host} --reassignment-json-file {reassign_increase_file} --verify')

    restore_file = os.path.join(RUNTIME_DIR,'{}_restore.json'.format(topic_name))
    with open(restore_file, 'w') as file:
        file.write(output)

    print('可以执行如下命令恢复原状：')
    print(f'{reassign_script} --zookeeper {zookeeper_host} --reassignment-json-file {restore_file} --execute')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='增加 kafka topic 的 partition')
    parser.add_argument('zookeeper_host',help='zookeeper host')
    parser.add_argument('topic',help='topic name')
    args = parser.parse_args()
    increase_partition(args.topic,args.zookeeper_host)
