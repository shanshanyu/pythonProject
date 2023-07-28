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
import threading

MY_DIR = os.path.dirname(os.path.abspath(__file__))  #获取当前路径


def sa_threading(main_fun,thread_list):
    running_thread = list()

    #创建多个线程执行 trust 函数
    for thread in thread_list:
        t = threading.Thread(target=main_fun,args=(thread,))
        t.daemon = True
        t.start()
        running_thread.append(t)




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

    def copy_from_remote(self,remote_file,local_file,timeout=1800):
        self.connect()

        sftp = paramiko.SFTPClient.from_transport(self.client.get_transport())
        sftp.get_channel().settimeout(timeout)
        sftp.get(remote_file,local_file)



class Trust:
    def __init__(self,conf_file):
        self.conf = self.parse_conf(conf_file)
        self.ssh_params = self.conf['ssh_params']
        self.trust_user = self.conf['trust_user']
        self.local_program_dir = MY_DIR
        self.remote_program_dir = self.local_program_dir
        self.temp_ssh_dir = '/tmp'
        self.real_ssh_dir = '/root/.ssh' if self.trust_user == 'root' else '/home/{}/.ssh'.format(self.trust_user)
        self.real_authorized_keys = '{}/authorized_keys'.format(self.real_ssh_dir)
        self.ips = self.conf['ips']

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

    def self_trust(self):
        def trust(host):  #在 host 上执行自身免密并复制 authorized_keys 到 /tmp
            ssh_client = SSHClient(**self.ssh_params[host])
            trust_cmd = '/bin/bash {}/script/self_trust.sh'
            res = ssh_client.run_cmd(trust_cmd)
            if res['ret'] != 0:
                raise Exception(res)

            #复制 authrized_keys 到 tmp 目录
            remote_temp_authorized_keys = '{}/{}_authorized_keys.{}'.format(self.temp_ssh_dir,self.trust_user,host)
            temp_keys_cmd = 'cp {} {}'.format(self.real_authorized_keys,remote_temp_authorized_keys)
            ssh_client.run_cmd(temp_keys_cmd)
            if res['ret'] != 0:
                raise Exception(res)

            local_host_authorized_keys = '{}/runtime/{}_authorized_keys.{}'.format(MY_DIR,self.trust_user,host)
            ssh_client.copy_from_remote(remote_temp_authorized_keys,local_host_authorized_keys)

        sa_threading(trust, 'self_trust', self.ips, wait_interval=2)


if __name__ == '__main__':
    t = Trust('../trust/test1.yml')
    print(t.conf)
    print(t.ssh_params)

'''
if __name__ == '__main__':
    client = SSHClient(hostname='10.129.20.81',username='root',password='MhxzKhl2015')
    result = client.run_cmd('lbn /')
    print(result)
'''


