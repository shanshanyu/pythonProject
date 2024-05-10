'''
create_time: 2023/6/28 15:35
author: yss
version: 1.0

测试脚本
'''
from kafka import KafkaConsumer


if __name__ == '__main__':
    consumer = KafkaConsumer('event_topic',bootstrap_servers='10.129.19.55:9092',group_id='sensor_debug')

    for msg in consumer:
        topic = msg.topic
        partition = msg.partition
        offset = msg.offset
        key = msg.key
        value = msg.value

        print(f'Received msg: topic={topic},partition={partition},offset={offset},key={key},value={value}')
