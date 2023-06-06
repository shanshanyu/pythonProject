'''
create_time: 2023/6/5 18:52
author: yss
version: 1.0
'''
import paramiko

# 创建 SSH 客户端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程主机
client.connect(hostname='123.56.222.255', username='yushanshan', password='xx',port=30022)

# 执行命令，启用伪终端模式
stdin, stdout, stderr = client.exec_command('ls /', get_pty=True)

# 输入命令（如果需要）
stdin.write('cat /etc/passwd\n')
stdin.flush()

# 获取输出
output = stdout.read().decode('utf-8')

# 打印输出
print(output)

# 关闭 SSH 连接
client.close()
