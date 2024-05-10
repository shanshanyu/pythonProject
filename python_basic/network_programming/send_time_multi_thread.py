'''
create_time: 2024/5/8 17:30
author: yss
version: 1.0

desc: 多线程的方式发送时间的服务端代码

来一个客户端创建一个子线程??
'''
import threading
from socket import socket,AF_INET,SOCK_STREAM
from datetime import datetime


class SendTime(threading.Thread):
    def __init__(self,sock):
        super().__init__()
        self.sock = sock

    def run(self) -> None:
        cur_time = datetime.now()
        cur_time = str(cur_time).encode('utf-8')
        self.sock.send(cur_time)


def main():
    server_sock = socket(AF_INET,SOCK_STREAM)
    server_sock.bind(('127.0.0.1',8888))
    server_sock.listen(128)
    print('服务器监听在 127.0.0.1:8888')

    while True:
        client_sock,client_addr = server_sock.accept()
        m = SendTime(client_sock)
        m.start()


if __name__ == '__main__':
    main()
