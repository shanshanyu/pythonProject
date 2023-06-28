'''
create_time: 2023/6/28 16:17
author: yss
version: 1.0
'''
#拉取partition末尾的1w行数据

from kafka import KafkaConsumer,TopicPartition

def get_msg(topic_name,bootstrap_servers,length):
    consumer = KafkaConsumer(topic_name,bootstrap_servers=bootstrap_servers)  #获取consumer
    partitions = consumer.partitions_for_topic(topic_name)  #获取partition

    last_recods = []

    for partition in partitions:
        tp = TopicPartition(topic_name,partition)  #获取 partition

        consumer.seek_to_end(tp)
        offset_end = consumer.position(tp)  #获得结尾的 offset
        consumer.seek_to_beginning(tp)
        offset_start = consumer.position(tp)  #获得开始的 offset

        offset = offset_end-length if offset_end-length > offset_start else offset_start   #python 中实现三目运算符的效果
        consumer.seek(tp,offset)

        for msg in consumer:
            #last_recods.append(msg.value.decode())
            last_recods.append(msg)
            if msg.offset == offset_end - 1:  #如果读到结尾了就退出
                break

    consumer.close()
    return last_recods

if __name__ == '__main__':
    topic_name = 'event_topic'
    bootstrap_servers = '10.129.19.55:9092'
    length = 10
    last_records = get_msg(topic_name,bootstrap_servers,length)


    for record in last_records:
        print(record)
