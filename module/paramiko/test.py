'''
create_time: 2023/5/8 15:30
author: yss
version: 1.0
'''

#SSHClient 的方式

import paramiko
client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.RejectPolicy())
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='123.56.222.255',port=30022,username='yushanshan',password='iflytek')
stdin,stdout,stderr = client.exec_command('df -h')
res = stdout.channel.recv_exit_status()
print('ret:',res)
print(type(stdout))
result = stdout.read()
client.close()

print(result.decode(encoding='utf-8'))