'''
create_time: 2024/5/6 11:55
author: yss
version: 1.0

desc: 获取时间的客户端程序
'''
from socket import socket,AF_INET,SOCK_STREAM


def main():
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.1',8888))
    data = client.recv(1024)
    print(data.decode('utf-8'))


if __name__ == '__main__':
    main()
