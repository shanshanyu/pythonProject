'''
create_time: 2024/5/6 11:21
author: yss
version: 1.0

desc: 客户端连接上来后，返回当前时间给客户端
'''
import datetime
import time
from socket import socket,AF_INET,SOCK_STREAM


def main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.bind(('127.0.0.1',8888))
    server_socket.listen()
    print('服务器已经监听在 127.0.0.1 8888 端口')
    # 服务端等待连接进入

    while True:
        client_socket,client_addr = server_socket.accept()
        cur_time = time.strftime('%Y/%m/%d-%H:%M:%S',time.localtime())
        client_socket.send(f'当前时间：{cur_time}'.encode('utf-8'))


if __name__ == '__main__':
    print(datetime.datetime.now())
    main()