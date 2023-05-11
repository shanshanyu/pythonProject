'''
create_time: 2023/5/9 10:14
author: yss
version: 1.0
'''

#通过 SFTPClient 封装 transport 的方式下载文件

import paramiko
transport = paramiko.Transport(('123.56.222.255',30022))
transport.connect(username='yushanshan',password='iflytek')

sftp = paramiko.SFTPClient.from_transport(transport)  #SFTPClient 是一个类方法

sftp.get('test.log','/Users/yushanshan/Downloads/test.log')

sftp.close()