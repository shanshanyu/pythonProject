'''
create_time: 2023/11/21 17:54
author: yss
version: 1.0

测试脚本
'''

from kafka import TopicPartition,KafkaConsumer
from datetime import datetime,timedelta
import argparse


def get_offset_by_time(topic_name,bootstrap_servers,timestamp):  #根据timestamp 找 offset
    consumer = KafkaConsumer(topic_name,bootstrap_servers=bootstrap_servers)
    partitions = consumer.partitions_for_topic(topic_name)  #获取 topic 有哪些 partitions

    offsets = {}

    for partition in partitions:
        tp = TopicPartition(topic_name,partition)  #TopicPartition 对象
        offsets[tp] = consumer.offsets_for_times({tp:timestamp})  #值是一个字典，键是TopicPartition对象，值是OffsetAndTimestamp对象

    consumer.close()
    return offsets


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='订阅kafka某个时间点的数据')
    parser.add_argument('topic_name', help='输入topic_name,比如event_topic')
    parser.add_argument('bootstrap_servers', help='输入kafka broker 的地址，比如10.1.1.1:9092')
    parser.add_argument('start_hour', help='输入小时，比如2023062800')
    args = parser.parse_args()

    time_start = datetime.strptime(args.start_hour, '%Y%m%d%H')  # 获得 datetime 对象,start_time
    start_offsets = get_offset_by_time(args.topic_name,args.bootstrap_servers,time_start.timestamp()*1000)
    for item in start_offsets.values():
        for key,value in item.items():
            if not value :
                print(f'{key.partition}:该partition没有数据')
            else:
                print(f'{key.partition}:{value.offset}')