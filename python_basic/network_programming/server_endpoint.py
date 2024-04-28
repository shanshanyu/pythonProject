'''
2024/4/28 21:42

desc: tcp 服务端的代码
'''
from socket import socket,AF_INET,SOCK_STREAM


def main():
    server_socket = socket(AF_INET,SOCK_STREAM)  # 创建服务端 socket
    server_socket.bind(('127.0.0.1',8888))  # 绑定地址
    server_socket.listen(5)
    print('server start success,waiting client connect ...')
    while True:
        #  每当接收到客户端的 socket 请求
        client_socket,client_addr = server_socket.accept()
        data = server_socket.recv(1024)
        print('客户端发送的数据是: ',data.decode('utf-8'))
        client_socket.send('收到了'.encode('utf-8'))
        break


if __name__ == '__main__':
    main()
