'''
create_time: 2023/6/5 14:07
author: yss
version: 1.0
'''


import paramiko
class SSHClient(object):
    def __init__(self,host,port=22,user='root',password=None,key_filename=None,encoding='utf-8',timeout=20):
        self.host = host
        self.user = user
        self.encoding = encoding

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

    def run_cmd(self,cmd,timeout=5):
        self.connect()
        stdin_fd,stdout_fd,stderr_fd = self.client.exec_command(cmd,timeout,get_pty=True)
        stdout, stderr = stdout_fd.read().decode('utf-8'), stderr_fd.read().decode('utf-8')
        ret = stdout_fd.channel.recv_exit_status()
        return {'ret': ret,'stdout': stdout,'stderr': stderr}









if __name__ == '__main__':
    client = SSHClient(host='123.56.222.255',port=30022,user='yushanshan',password='xx')
    client.connect()
    ret = client.run_cmd('df -h /')
    print(ret)