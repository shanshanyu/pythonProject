'''
create_time: 2023/5/11 10:45
author: yss
version: 1.0
'''
import os.path
import re
import threading

import paramiko
import psutil


def check_ip(ip):
    '''
    :检查给定的字符串是否是 ip
    :param ip:
    :return:
    '''
    #p = re.compile('^((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$')
    p = re.compile('^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9])(\.25[0-5]|\.2[0-4]\d|\.1\d\d|\.[1-9]\d|\.\d){3}$')
    if p.match(ip):
        return True
    else:
        return False


def get_self_ip(ips):  #获取本机 ip，找到了返回 ip，如果没有找到抛出异常
    local_address = [address[1][0].address for address in psutil.net_if_addrs().items()]
    for address in local_address:
        if address in ips:
            ip = address
            break
    else:
        raise Exception('local_ip not in ips')

    return ip


def sa_threading(main_fun,action_name,thread_list,done_counter='done'):
    running_threads = list()
    counters = dict()
    lock = threading.Lock()

    def main_wrapper(key,counters,lock):
        if type(counters) != dict:
            raise Exception('keyError: {} should be a dict.'.format(counters))

        try:
            return main_fun(key,counters,lock)
        except Exception as e:
            with lock:
                counters['error']  = 1

    for thread in thread_list:
        t = threading.Thread(target=main_wrapper,name=thread,args=(thread,counters,lock))





#定义 SSHClient 类，用来管理 ssh client，不需要手动释放连接
class SSHClient(object):
    def __init__(self,host,port=22,user='root',password=None,key_filename=None,encoding='utf-8',timeout=10): #连接超时 10s
        self.hostname = host
        self.user = user
        self.encoding = encoding
        #判断 key_file 的用户名,key_filename 感觉没用
        '''if not key_filename and user != 'root':
            key_file = '/home/{}/.ssh/id_ida'.format(user)
            if not os.path.exists(key_file):
                key_file = None
        '''
        self.params = {
            'hostname': host,
            'port': port,
            'username': user,
            'password': password,
            'key_filename': key_filename,
            'timeout': timeout
        }

        #创建 SSHClient
        self.client = paramiko.SSHClient()
        #加载 know hosts，没啥用
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.is_connected = False

    #在 __init__ 中建立的连接，在 del 中要释放
    def  __del__(self):
        try:
            self.client.close()
        except Exception:
            pass

    def check_paramiko(self,cmd):
        '''
        :检查是否能登录机器并执行命令
        :param cmd:
        :return:
        '''
        res = self.run_cmd(cmd)
        if res['ret'] == 0:
            return True,res
        else:
            return False,res


    def connect(self):
        '''
        :连接服务器
        :return:
        '''
        if self.is_connected:
            return True
        try:
            self.client.connect(**self.params)
            self.is_connected = True
        except Exception as e:
            print(e)

    def run_cmd(self,cmd,timeout=15):  #命令执行超时 15s
        '''
        :执行命令
        :param cmd:
        :param timeout:
        :return:
        '''
        #如果
        self.connect()

        stdin_fd,stdout_fd,stderr_fd = self.client.exec_command(cmd,timeout=timeout,get_pty=True)
        ret = stdout_fd.channel.recv_exit_status()
        stdout,stderr = stdout_fd.read().decode(self.encoding),stderr_fd.read().decode(self.encoding)
        return {'ret':ret,'stdout':stdout,'stderr':stderr}

    def get_transport(self):  #获取 transport
        return self.client.get_transport()


    def copy_from_local(self,local_file,remote_file,timeout=1800): #从本地复制文件到远端
        self.connect()

        sftp = paramiko.SFTPClient.from_transport(self.client.get_transport())
        sftp.get_channel().settimeout(timeout)
        sftp.put(local_file,remote_file)
        sftp.close()

    def copy_from_remote(self,remote_file,local_file,timeout=1800): #从远端复制文件到本地
        self.connect()

        sftp = paramiko.SFTPClient.from_transport(self.client.get_transport())
        sftp.get_channel().settimeout(timeout)
        sftp.get(remote_file,local_file)
        sftp.close()



