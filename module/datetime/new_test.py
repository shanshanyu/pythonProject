'''
create_time: 2023/6/28 17:25
author: yss
version: 1.0
'''


from datetime import datetime,timedelta
from kafka import KafkaConsumer,TopicPartition

time_str = '2023062817'


def subscribe_topic(topic_name,bootstrap_servers,hour):
    time_start = datetime.strptime(hour,'%Y%m%d%H')   #获得 datetime 对象,start_time
    end_time = time_start + timedelta(hours=1)    #end_time

    consumer = KafkaConsumer(topic_name,bootstrap_servers)

    partitions = consumer.partitions_for_topic(topic_name)  #partitions 是一个集合
    print(partitions,type(partitions))

    messages = []

    for partition in partitions:
        tp = TopicPartition(topic_name,partition)  #获得partition 对象







if __name__ == '__main__':
    topic_name = 'event_topic'
    bootstrap_servers = '10.129.19.55:9092'
    hour = '2023061817'

    subscribe_topic(topic_name,bootstrap_servers,hour)