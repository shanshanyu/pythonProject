'''
create_time: 2024/3/13 20:42
author: yss
version: 1.0
desc: redis 客户端的操作
'''

from rediscluster import RedisCluster


def main():
    #生成客户端连接
    redis_nodes = [
        {'host':'172.19.229.90','port':'7001'},
        {'host' : '172.19.229.90', 'port':'7002'},
        {'host' : '172.19.229.90', 'port':'7003'}
    ]
    try:
        rc = RedisCluster(startup_nodes=redis_nodes,decode_responses=True)
        rc.set('dd','5678')
        print(rc.get('dd'))
    except Exception as e:
        print(e)
    finally:
        rc.close()

if __name__ == '__main__':
    main()

