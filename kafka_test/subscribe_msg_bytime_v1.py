'''
create_time: 2023/6/28 18:21
author: yss
version: 1.0
'''

#订阅某个 topic  某个时间点的数据，时间点是小时
from kafka import KafkaConsumer,TopicPartition
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
    return offsets  #offsets 是一个字典


def subscribe_topic(bootstrap_servers,start_offset,end_time):
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)

    #assign partition
    consumer.assign(start_offset.keys()) #如果不用 assign，需要先获取partition元数据，然后再通过调用seek(partion，offset)

    for item in start_offset.values(): #设置seek 的 offset
        for key, value in item.items():
            consumer.seek(key,value.offset)


    end_timestamp = end_time.timestamp()*1000

    messages = []  #消息列表

    for msg in consumer:
        if msg.timestamp >= end_timestamp:
            break
        messages.append(msg.value.decode())

    consumer.close()
    return messages


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='订阅kafka某个时间点的数据')
    parser.add_argument('topic_name',help='输入topic_name,比如event_topic')
    parser.add_argument('bootstrap_servers',help='输入kafka broker 的地址，比如10.1.1.1:9092')
    parser.add_argument('hour',help='输入小时，比如2023062818')
    args = parser.parse_args()

    time_start = datetime.strptime(args.hour, '%Y%m%d%H')  # 获得 datetime 对象,start_time
    end_time = time_start + timedelta(hours=1)  # end_time
    #print(time_start.timestamp()*1000,type(time_start.timestamp()))
    start_offset = get_offset_by_time(args.topic_name,args.bootstrap_servers,time_start.timestamp()*1000)
    #print(start_offset)
    messages = subscribe_topic(args.bootstrap_servers,start_offset,end_time)

    for msg in messages:
        print(msg)





