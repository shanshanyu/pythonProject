'''
create_time: 2023/7/27 14:14
author: yss
version: 1.0
'''

from kafka import TopicPartition,KafkaConsumer
from datetime import datetime,timedelta
import argparse
import threading


def subscribe_partition(partition,offset,bootstrap_servers,end_time):
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    consumer.assign([partition])
    consumer.seek(partition,offset.offset)

    max_offset = max(consumer.end_offsets([partition]).values())

    for msg in consumer:
        if msg.timestamp >= end_time or msg.offset >= max_offset-1:
            break
        print(msg.value.decode())

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
    flag = False
    for i in start_offsets.values():
        for k,v in i.items():
            if v:
                flag = True
                t = threading.Thread(target=subscribe_partition,args=(k,v,bootstrap_servers,end_time))  #传递 TopicPartition 对象
                threads.append(t)
                t.start()

    if not flag:
        print('指定的时间点找不到数据，检查输入的时间是否正确以及服务器的时间')

    for t in threads:
        t.join()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='订阅kafka某个时间点的数据')
    parser.add_argument('topic_name', help='输入topic_name,比如event_topic')
    parser.add_argument('bootstrap_servers', help='输入kafka broker 的地址，比如10.1.1.1:9092')
    parser.add_argument('start_hour', help='输入小时，比如2023062818')
    parser.add_argument('end_hour', help='输入小时，比如2023062820')
    args = parser.parse_args()

    time_start = datetime.strptime(args.start_hour, '%Y%m%d%H')  # 获得 datetime 对象,start_time
    time_end = datetime.strptime(args.end_hour, '%Y%m%d%H')  # 获得 datetime 对象,start_time
    #time_end = time_start + timedelta(hours=1)  # end_time
    print(time_start,time_end)

    subscribe_topic(args.topic_name,args.bootstrap_servers,time_start.timestamp()*1000,time_end.timestamp()*1000)






