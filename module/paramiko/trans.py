'''
create_time: 2023/5/8 18:42
author: yss
version: 1.0
'''

#Transport

import paramiko

transport = paramiko.Transport(('123.56.222.255',30022))  #transport需要传递元组
transport.connect(username='yushanshan',password='xx')


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client._transport = transport
stdin,stdout,stderr = client.exec_command('df -h')
result = stdout.read()
transport.close()
print(result.decode('utf-8'))