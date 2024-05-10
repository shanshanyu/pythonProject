'''
create_time: 2024/5/10 10:06
author: yss
version: 1.0

desc：客户端发送一个请求后，就把 telent.png 图片发送给客户端   网络上的数据传输得发送字节数据

把图片打开(二进制)->base64编码(二进制)->decode成字符串放入python对象中->python对象转换成json字符串->json字符串encode后发送给客户端

服务端监听->客户端请求到来，创建一个新的线程去发送数据
'''
import threading
from socket import socket,AF_INET,SOCK_STREAM
from base64 import b64encode,b64decode
import json


class SendPicThread(threading.Thread):
    def __init__(self,client,data):
        super().__init__()
        self.client = client
        self.data = data

    def run(self) -> None:
        '''
        发送图片给客户端
        :param client:
        :return:
        '''
        self.client.send(self.data)


def main():
    # 打开文件
    with open('telnet.png','rb') as f:
        data = f.read()

    # base64 编码
    data = b64encode(data)

    pic_data = {'filename':'telnet.png','data':data.decode('utf-8')}

    # python对象转换成json字符串
    pic_data = json.dumps(pic_data)

    # 转换成二进制
    pic_data = pic_data.encode('utf-8')

    try:
        server_sock = socket(AF_INET,SOCK_STREAM)
        server_sock.bind(('127.0.0.1',8888))
        server_sock.listen(128)
        print('服务器已经准备好..')

        while True:
            client_sock,client_addr = server_sock.accept()
            # 发送图片数据给客户端
            m = SendPicThread(client_sock,pic_data)
            m.start()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()






