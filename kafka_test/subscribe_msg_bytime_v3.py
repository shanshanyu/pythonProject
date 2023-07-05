'''
create_time: 2023/7/5 11:19
author: yss
version: 1.3
解决v1.1中的两个问题
画出来：
根据时间戳找offset->设置当前的offset->拉取数据
如果拉取到的offset等于当前partition最大的offset，编写一个函数判断是否所有的partition都达到最大offset
如果拉取到的时间等于截止时间，编写一个函数判断是否所有的partition都达到最大的时间

用多线程实现，每个线程拉取一个有数据的 partition
'''

from kafka import TopicPartition,KafkaConsumer
from datetime import datetime,timedelta
import argparse
import threading

messages = []
lock = threading.RLock()


def subscribe_partition(partition,offset,bootstrap_servers,end_time):
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    consumer.assign([partition])
    consumer.seek(partition,offset.offset)

    max_offset = max(consumer.end_offsets([partition]).values())

    for msg in consumer:
        if msg.timestamp >= end_time or msg.offset >= max_offset-1:
            break
        with lock:
            messages.append(msg)


    consumer.close()


def get_offset_by_time(topic_name,bootstrap_servers,timestamp):  #根据timestamp 找 offset
    consumer = KafkaConsumer(topic_name,bootstrap_servers=bootstrap_servers)
    partitions = consumer.partitions_for_topic(topic_name)  #获取 topic 有哪些 partitions

    offsets = {}

    for partition in partitions:
        tp = TopicPartition(topic_name,partition)  #TopicPartition 对象
        offsets[tp] = consumer.offsets_for_times({tp:timestamp})  #值是一个字典，键是TopicPartition对象，值是OffsetAndTimestamp对象

    consumer.close()
    return offsets


def subscribe_topic(topic_name,bootstrap_servers,start_time,end_time):
    # 获取指定时间戳的offset，start_offsets 结构中可能存在offset 为 None 的成员
    start_offsets = get_offset_by_time(topic_name,bootstrap_servers,start_time)

    threads = []
    for i in start_offsets.values():
        for k,v in i.items():
            if v:
                t = threading.Thread(target=subscribe_partition,args=(k,v,bootstrap_servers,end_time))  #传递 TopicPartition 对象
                threads.append(t)
                t.start()

    for t in threads:
        t.join()

    for msg in messages:
        print(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='订阅kafka某个时间点的数据')
    parser.add_argument('topic_name', help='输入topic_name,比如event_topic')
    parser.add_argument('bootstrap_servers', help='输入kafka broker 的地址，比如10.1.1.1:9092')
    parser.add_argument('hour', help='输入小时，比如2023062818')
    args = parser.parse_args()

    time_start = datetime.strptime(args.hour, '%Y%m%d%H')  # 获得 datetime 对象,start_time
    time_end = time_start + timedelta(hours=1)  # end_time

    subscribe_topic(args.topic_name,args.bootstrap_servers,time_start.timestamp()*1000,time_end.timestamp()*1000)






