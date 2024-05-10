'''
create_time: 2024/5/10 11:41
author: yss
version: 1.0
'''


from socket import socket,AF_INET,SOCK_STREAM
from base64 import b64decode


def main():
    try:
        client_sock = socket(AF_INET,SOCK_STREAM)
        client_sock.connect(('127.0.0.1',8888))
        data = client_sock.recv(1024)
        pic_data = b''
        while data:
            pic_data += data

        pic_data = pic_data.decode('utf-8')

    except Exception as e:
        print(e)

    filename = pic_data['filename']
    file_data = pic_data['data']

    with open(f'/tmp/{filename}','wb') as f:
        f.write(b64decode(file_data))