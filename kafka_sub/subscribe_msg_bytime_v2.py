'''
create_time: 2023/7/4 21:02
author: yss
version: 1.2

测试脚本

解决v1.1中的两个问题
画出来：
根据时间戳找offset->设置当前的offset->拉取数据
如果拉取到的offset等于当前partition最大的offset，编写一个函数判断是否所有的partition都达到最大offset
如果拉取到的时间等于截止时间，编写一个函数判断是否所有的partition都达到最大的时间
'''

from kafka import TopicPartition,KafkaConsumer
from datetime import datetime,timedelta
import argparse


def is_over_by_time():
    pass

def is_over_by_offset():
    pass

def get_offset_by_time(topic_name,bootstrap_servers,timestamp):
    consumer = KafkaConsumer(topic_name,bootstrap_servers=bootstrap_servers)
    partitions = [TopicPartition(topic_name,partition) for partition in consumer.partitions_for_topic(topic_name)] #列表表达式获取或有的partition对象

    end_offsets = consumer.end_offsets(partitions)
    start_offsets = {}
    for p in partitions:
        start_offsets[p] = consumer.offsets_for_times({p:timestamp})

    consumer.close()
    return start_offsets,end_offsets
    #{TopicPartition(topic='event_topic', partition=0): 224215....},{TopicPartition:{TopicPartition:OffsetAndTimestamp}....}


def subscribe_topic(topic_name,bootstrap_servers,start_offsets,end_offsets,end_timestamp):
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    consumer.assign(start_offsets.keys())  #keys()是 TopicPartition 的列表

    #判断字典所有的value是否都为 None,如果不为None，设置拉取的offset
    flag = False
    for offsets in start_offsets.values():
        for key,val in offsets.items():  #key= TopicPartition  val= offsets
            if val:
                consumer.seek(key,val)
                flag = True
                break

    if not flag:
        print('指定的时间拉取不到数据，请确认时间输入是否正确以及服务器时间')
        exit(1)

    messages = []



    for msg in consumer:
        if msg.timestamp >= end_timestamp: #判断是否所有的partition都超过 end_time
            pass
        if msg.offset >= end_offsets[TopicPartition(topic_name,msg.partition)]: #判断是否所有的partition都超过end_offsets
            pass

        messages.append(msg.value.decode())

    return messages









if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='订阅kafka某个时间点的数据')
    parser.add_argument('topic_name', help='输入topic_name,比如event_topic')
    parser.add_argument('bootstrap_servers', help='输入kafka broker 的地址，比如10.1.1.1:9092')
    parser.add_argument('hour', help='输入小时，比如2023062818')
    args = parser.parse_args()

    time_start = datetime.strptime(args.hour, '%Y%m%d%H')  # 获得 datetime 对象,start_time
    time_end = time_start + timedelta(hours=1)  # end_time
    # print(time_start.timestamp()*1000,type(time_start.timestamp()))
    start_offsets,end_offsets = get_offset_by_time(args.topic_name, args.bootstrap_servers, time_start.timestamp() * 1000)
    # print(start_offset)
    messages = subscribe_topic(args.topic_name,args.bootstrap_servers, start_offsets,end_offsets,time_end)

    for msg in messages:
        print(msg)



