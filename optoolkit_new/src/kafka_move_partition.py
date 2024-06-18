'''
create_time: 2024/4/25 14:44
author: yss
version: 1.0

desc: kafka 磁盘间 partition 迁移

usage: 需要输入 zk 地址，需要迁移 partition 所在节点的主机名
'''
from kazoo.client import KazooClient
import json
import os
import subprocess
import argparse


def get_kafka_broker_host2id(zookeeper_host):
    # 创建Kazoo客户端
    zk = KazooClient(hosts=zookeeper_host)

    # 连接到ZooKeeper服务器
    zk.start()

    # 获取Kafka的Broker ID
    broker_id_list = None

    # 存储 id host 的映射dict
    host2id = {}

    try:
        broker_id_list = zk.get_children("/brokers/ids")
        for i in broker_id_list:
            data = zk.get(f'/brokers/ids/{i}')
            data = json.loads(data[0].decode())  # 获取的数据转换成字典
            data = data['host']
            host2id[data] = i
    except Exception as e:
        print(f"Error: {e}")

    # 关闭ZooKeeper连接
    zk.stop()
    return host2id  # 返回值是 dict


def get_reassign_script():
    reassign_script = '/data/sa_cluster/cloudera/parcels/KAFKA-4.1.0-1.4.1.0.p0.4/lib/kafka/bin/kafka-reassign-partitions.sh'

    if os.path.exists(
            '/data/sa_cluster/cloudera/parcels/KAFKA-4.1.0-1.4.1.0.p0.4/lib/kafka/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/data/sa_cluster/cloudera/parcels/KAFKA-4.1.0-1.4.1.0.p0.4/lib/kafka/bin/kafka-reassign-partitions.sh'
    elif os.path.exists('/sensorsdata/main/program/sp/sdp/1.0.0.0-123/kafka/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/sensorsdata/main/program/sp/sdp/1.0.0.0-123/kafka/bin/kafka-reassign-partitions.sh'
    elif os.path.exists(
            '/sensorsdata/main/program_entity/kafka/artifacts/kafka_core/2.8.1.3094/bin/kafka-reassign-partitions.sh'):
        reassign_script = '/sensorsdata/main/program_entity/kafka/artifacts/kafka_core/2.8.1.3094/bin/kafka-reassign-partitions.sh'

    if not os.path.exists(reassign_script) :
        print('kafka-reassign-partitions.sh 脚本路径找不到，不能使用此脚本')
        exit(1)

    return reassign_script


class KafkaPartitionMove(object):
    def __init__(self,zookeeper_host,topic_name,dest_partition,dest_host,dest_disk):
        self.zookeeper_host = zookeeper_host
        self.host2id = get_kafka_broker_host2id(zookeeper_host)
        self.topic_name = topic_name  # 需要操作的 topic_name
        self.dest_partition = int(dest_partition)  # 需要操作的 partition
        self.dest_host = self.get_fqdn(dest_host)# 目标 host
        self.dest_disk = dest_disk  # 目标 dist
        self.broker_host_url = self.dest_host + ':9092'
        self.broker_id_str = ','.join(list(self.host2id.values()))
        self.broker_host_str = ','.join(list(self.host2id.keys()))  # broker str,纯字符串
        self.reassign_script = get_reassign_script()  # 获取 reassign 脚本路径

    def get_fqdn(self,dest_host):
        for host in self.host2id.keys():
            if dest_host in host:
                return host
        return ''

    def move_partition(self):
        topic_json = '{"topics": [{"topic": "%s"}],"version": 1}' % self.topic_name  # 格式化字符串
        reassign_file = os.path.join('runtime', '{}.json'.format(self.topic_name))

        with open(reassign_file, 'w') as f:  # 创建文件写入 json 数据
            f.write(topic_json)

        reassign_cmd = f'{self.reassign_script} --zookeeper {self.zookeeper_host} --topics-to-move-json-file {reassign_file} ' \
                       f'--broker-list {self.broker_id_str}  --generate |grep Current -A 1|grep -v Current'

        output = ''
        try:
            completed_process = subprocess.run(reassign_cmd, shell=True, text=True, stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
            output = completed_process.stdout
        except Exception as e:
            print(f"执行命令时出错: {str(e)}")

        output_obj = json.loads(output)  # json 字符串转成 python 对象

        current_assign_file = os.path.join('runtime', '{}.json'.format(self.topic_name+'_current_assign'))
        with open(current_assign_file,'w') as f:
            f.write(output)

        partition_list = output_obj['partitions']  # 获得 partitions 列表

        flag = False  # 加个标志
        for partition in partition_list:
            partition_id = int(self.host2id[self.dest_host])
            if partition['partition'] == self.dest_partition and partition_id in partition['replicas']:  # 指定主机上有这个 partition 才能更改 logs_dir
                index = partition['replicas'].index(partition_id)
                partition['log_dirs'][index] = self.dest_disk
                flag = True

        if not flag:
            print('指定的 partition 不存在，或目标主机上没有该 partition')
            exit(1)

        ultra_assign_file = os.path.join('runtime', '{}.json'.format(self.topic_name+'_ultra_assign'))
        with open(ultra_assign_file,'w') as f:
            f.write(json.dumps(output_obj))

        reassign_cmd_exec = f'{self.reassign_script} --zookeeper {self.zookeeper_host} --reassignment-json-file {ultra_assign_file} --bootstrap-server {self.broker_host_url} --execute'

        err = ''
        try:
            completed_process = subprocess.run(reassign_cmd_exec, shell=True, text=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            err = completed_process.stderr
        except Exception as e:
            print(f"执行命令时出错: {str(e)}")

        if err:
            print('不妙，有异常！！')
            print(err)
            exit(1)
        print('{} 迁移副本命令完成，使用如下命令检查扩容结果：'.format(self.topic_name))
        print(f'{self.reassign_script} --zookeeper {self.zookeeper_host} --reassignment-json-file {ultra_assign_file} --bootstrap-server {self.broker_host_url} --verify')
        print('使用如下命令回滚：')
        print(f'{self.reassign_script} --zookeeper {self.zookeeper_host} --reassignment-json-file {current_assign_file} --bootstrap-server {self.broker_host_url} --execute')


def exec_move_partition():
    print('输入参数示例： zookeeper_host  topic_name  partition_id  dest_host  dest_disk')
    print('hybrid01  event_topic  14  hybrid02  /sensorsdata/seqdata02/kafka/data  表示将 hybrid02 节点 event_topic 14 从其他盘移动到 /sensorsdata/seqdata02 盘')
    input_args = input()
    input_args_lst = input_args.split()
    m = KafkaPartitionMove(input_args_lst[0], input_args_lst[1], input_args_lst[2], input_args_lst[3], input_args_lst[4])
    m.move_partition()


def main():
    parser = argparse.ArgumentParser(description='迁移 kafka topic 的 partition')
    parser.add_argument('zookeeper_host', help='zookeeper host')
    parser.add_argument('topic_name', help='需要调整的 topic name')
    parser.add_argument('partition_id',help='需要迁移的 partition id')
    parser.add_argument('dest_host',help='需要迁移 partition 的主机名')
    parser.add_argument('dest_disk',help='需要把 partition 迁移到哪块盘')
    args = parser.parse_args()

    m = KafkaPartitionMove(args.zookeeper_host,args.topic_name,args.partition_id,args.dest_host,args.dest_disk)
    m.move_partition()


if __name__ == '__main__':
    main()