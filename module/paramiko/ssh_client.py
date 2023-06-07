'''
create_time: 2023/6/5 14:07
author: yss
version: 1.0
'''

import sys
import time
import paramiko
class SSHClient(object):
    def __init__(self,host,port=22,user='root',password=None,key_filename=None,timeout=15):#连接超时15s
        self.host = host
        self.user = user

        self.params = {
            'hostname':host,
            'port':port,
            'username':user,
            'password':password,
            'key_filename':key_filename,
            'timeout':timeout
        }
        #创建ssh client
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.is_connected = False

    #关闭连接
    def __del__(self):
        try:
            self.client.close()
        except Exception as e:
            print(e)

    #建立连接
    def connect(self):
        if self.is_connected:
            return True
        try:
            self.client.connect(**self.params)
            self.is_connected = True
        except Exception as e:
            print(e)
            exit(1)  #节点连接不上，直接退出

    def run_cmd(self,cmd,timeout=60):  #命令执行超时时间 60s
        self.connect()
        stdin_fd,stdout_fd,stderr_fd = self.client.exec_command(cmd,timeout,get_pty=True)
        stdout, stderr = stdout_fd.read().decode('utf-8'), stderr_fd.read().decode('utf-8')
        ret = stdout_fd.channel.recv_exit_status()
        return {'ret': ret,'stdout': stdout,'stderr': stderr}

    def check_paramiko(self,cmd='echo Hello!'):  #检查是否能登录
        res = self.run_cmd(cmd)
        if res['ret'] == 0:
            return True,res
        else:
            return False,res

    def get_transport(self): #获取 transport
        self.connect()

        return self.client.get_transport()

    def invoke_shell(self):
        self.connect()

        return self.client.invoke_shell('linux')












if __name__ == '__main__':


    client = SSHClient(host='10.129.19.55',port=22,user='sa_cluster',password='KJyOD8LjzN72')
    client.connect()
    ret = client.check_paramiko()
    if ret[0]:
        print('login success')
    else:
        print('can not connect')
        sys.exit(1)

    channel = client.invoke_shell()
    while True:
        time.sleep(0.1)

        if not channel.exit_status_ready():
            data = channel.recv(10240).decode('utf-8')
            print(data,end='')
            sys.stdout.flush()

        if not channel.exit_status_ready():
            cmd = input()
            if cmd == 'quit':
                exit(0)
            channel.send(cmd+'\r')
            sys.stdin.flush()







