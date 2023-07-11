'''
create_time: 2023/7/11 09:34
author: yss
version: 1.0
sdg 自动化分析工具：
当前版本支持分析元数据类问题
'''
from hyperion_client.hyperion_inner_client.inner_deploy_topo import InnerDeployTopo
from hyperion_client.node_info import NodeInfo
import threading
import json
import paramiko
import os

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
    def __del__(self):
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

    def run_cmd(self, cmd, timeout=15) :  # 命令执行超时 15s
        '''
        :执行命令
        :param cmd:
        :param timeout:
        :return:
        '''
        # 如果
        self.connect()

        stdin_fd, stdout_fd, stderr_fd = self.client.exec_command(cmd, timeout=timeout, get_pty=True)
        stdout, stderr = stdout_fd.read().decode(self.encoding), stderr_fd.read().decode(self.encoding)
        ret = stdout_fd.channel.recv_exit_status()
        return {'ret' : ret, 'stdout' : stdout, 'stderr' : stderr}

    def get_transport(self) :  # 获取 transport
        return self.client.get_transport()


def thr_func(host, port, data) :
    ssh_client = SSHClient(host, port, 'sa_cluster')
    log_path = os.environ.get('SENSORS_DATA_GOVERNOR_LOG_DIR')
    log_file = os.path.join(log_path, 'web', 'web.log')
    print(log_file)
    cmd = f'tail -1000000 {log_file}'
    print(cmd)

    res = ssh_client.run_cmd(cmd)
    # print('stdout',res['stdout'])
    # print('stderr', res['stderr'])

    for line in res['stdout'].split('\n') :
        for key in data :
            if key in line :
                print('发现问题,解决方法：', data[key])


def analysis() :
    host_lst = InnerDeployTopo().get_host_list()
    host_num = len(host_lst)

    port = NodeInfo().get_node_ssh_port(hostname=host_lst[0])
    # print(port)

    # json知识库
    with open('sdg.json', 'r') as f :
        data = json.load(f)
        # print(data)

    threads = []

    # 创建多线程解析日志
    for i in range(host_num) :
        t = threading.Thread(target=thr_func, args=(host_lst[i], port, data))
        t.start()
        threads.append(t)

    for t in threads :
        t.join()


if __name__ == '__main__' :
    analysis()