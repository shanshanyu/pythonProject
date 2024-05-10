'''
create_time: 2024/5/10 11:41
author: yss
version: 1.0

desc: 客户端获取图片
服务端发送完图片数据后关闭连接->客户端接收数据(二进制数据)->解码成字符串(字符串)->json字符串转换成json对象->二进制数据写入文件
'''


from socket import socket,AF_INET,SOCK_STREAM
from base64 import b64decode
import json


def main():
    try:
        client_sock = socket(AF_INET,SOCK_STREAM)
        client_sock.connect(('127.0.0.1',8888))
        data = client_sock.recv(1024)
        pic_data = b''

        while data:
            pic_data += data
            data = client_sock.recv(1024)
        # 转换成json字符串
        pic_data = pic_data.decode('utf-8')

    except Exception as e:
        print(e)

    pic_data = json.loads(pic_data)
    filename = pic_data['filename']
    file_data = pic_data['data']

    with open(f'/tmp/{filename}','wb') as f:
        f.write(b64decode(file_data))

    print('图片已保存')


if __name__ == '__main__':
    main()