'''
create_time: 2023/7/24 11:17
author: yss
version: 1.0
ssh免密脚本
'''
import os.path
import sys
import paramiko
import yaml


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


class Trust:
    def __init__(self,conf_file):
        self.conf = self.parse_conf(conf_file)

    def parse_conf(self,conf_file):
        #print(os.path.abspath(conf_file))
        if not os.path.exists(conf_file):   #判断文件是否存在
            raise Exception('{} 文件不存在'.format(conf_file))

        with open(conf_file,'r') as f:  #解析文件
            try:
                conf = yaml.full_load(f.read())
            except Exception as e:
                print(e)

        required_keys = ['ips','ssh_port','password','user','trust_user']
        list_type_keys = ['ips','password']

        for i in required_keys:
            if i not in conf.keys():
                print('配置文件错误,{}不存在'.format(i))
                sys.exit(1)

        for i in list_type_keys:
            if not isinstance(conf[i],list):
                print('{} 需要是列表类型'.format(i))
                sys.exit(1)

        if len(conf['ips']) != len(conf['password']):
            print('ip 和 密码长度不相等')
            sys.exit(1)

        conf['ssh_params'] = {}
        for i in conf['ips']:
            conf['ssh_params'][i] = {'hostname':i,'port':conf['ssh_port'],'username':conf['user'],'password':conf['password'][conf['ips'].index(i)]}

        return conf


if __name__ == '__main__':
    t = Trust('../trust/test1.yml')
    print(t.conf)

'''
if __name__ == '__main__':
    client = SSHClient(hostname='10.129.20.81',username='root',password='MhxzKhl2015')
    result = client.run_cmd('lbn /')
    print(result)
'''


