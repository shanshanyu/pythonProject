'''
create_time: 2024/12/25 11:26
author: yss
version: 1.0
desc: 计算 zk 节点的个数
'''
from kazoo.client import KazooClient


def count_child_recursively(zk,path):
    count = 0
    try:
        children = zk.get_children(path)
        count = len(children)
        for child in children:
            count += count_child_recursively(zk,f"{path}/{child}")
    except Exception as e:
        print(e)
    return count


def print_child_count(path):
    # 创建 zk 客户端
    zk = KazooClient(hosts='127.0.0.1:2181')
    # 连接到 zk 服务器
    zk.start(timeout=10)

    node_list = zk.get_children(path)

    for node in node_list:
        if path == '/':
            count = count_child_recursively(zk, f"/{node}")
            print(f"/{node}", count)
        else:
            count = count_child_recursively(zk, f"{path}/{node}")
            print(f"{path}/{node}", count)

    zk.stop()


if __name__ == '__main__':
    print_child_count('/sensors_analytics')