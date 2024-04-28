'''
Data: 2024/4/28 21:59
Author: yss
Desc: TCP 客户端
'''


from socket import socket,AF_INET,SOCK_STREAM


def main():
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect(('127.0.0.1',8888))
    client_socket.send('给你一个大笔都'.encode('utf-8'))
    data = client_socket.recv(1024)
    print('收到了: ',data.decode('utf-8'))
    client_socket.close()


if __name__ == '__main__':
    main()