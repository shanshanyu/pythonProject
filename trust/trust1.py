'''
create_time: 2023/7/24 11:17
author: yss
version: 1.0
ssh免密脚本
'''

import paramiko


class SSHClient:
    '''
    ;用来建立一个 ssh_client，不需要人为手动关闭连接

    '''
    def __init__(self,hostname,port=22,username=None,password=None,timeout=15,encoding='utf-8'):
        self.encoding = encoding
        self.params = {
            'hostname':hostname,
            'port':port,
            'username':username,
            'password':password,
            'timeout':timeout,
        }
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.connected = False

    def __del__(self):
        try:
            self.client.close()
        except:
            pass

    def connect(self):
        if self.connected:
            return True
        self.client.connect(**self.params)

    def run_cmd(self,cmd,timeout=15):
        if not self.connected:  #如果没有建立连接，先建立连接
            self.connect()
        try:
            fd_stdin,fd_stdout,fd_stderr = self.client.exec_command(cmd,timeout)
            stdout,stderr = fd_stdout.read().decode(self.encoding),fd_stderr.read().decode(self.encoding)
            ret = fd_stdout.channel.recv_exit_status() #获取退出状态
            return {'ret':ret,'stdout':stdout,'stderr':stderr}
        except paramiko.SSHException:
            print('命令执行失败')


if __name__ == '__main__':
    client = SSHClient(hostname='10.129.20.81',username='root',password='MhxzKhl2015')
    ret = client.run_cmd('ls /')
    print(ret)

