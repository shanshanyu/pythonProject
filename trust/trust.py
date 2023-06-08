'''
create_time: 2023/5/10 11:08
author: yss
version: 1.0
'''
import os.path
import os
import sys
import yaml
import json
from env_utils import check_ip,SSHClient
import logging





sys.argv.append('test.yml')
print(sys.argv)

WORK_DIR = os.path.dirname(os.path.abspath(__file__))  #获取文件所在目录
print(WORK_DIR)

class Trust(object):
    def __init__(self,conf_file):
        #用来保存conf的结果，方便后续问题排查
        self.conf_json = os.path.join(WORK_DIR,'trust.json')
        #conf，解析 conf_file 文件，返回值是一个 python 对象
        self.conf = self.parse_conf(conf_file)

        #将conf字典中的字段提取出来，方便后续直接调用
        self.ips = self.conf['ips']
        self.ssh_port = self.conf['ssh_port']


        # user 必须是 root，并且提供密码
        self.user = self.conf['user']
        self.trust_user = self.conf['trust_user']
        self.password = self.conf['password']
        self.ssh_params = self.conf['ssh_params']

        self.local_program_dir = os.path.basename(WORK_DIR)  #工作目录的名字
        self.program_tar_name = '{}.tar.gz'.format(self.local_program_dir)  #压缩包的名字
        self.local_program_tar = os.path.join(os.path.dirname(WORK_DIR),self.program_tar_name)

        self.remote_program_dir = self.local_program_dir  #远端目录
        self.remote_program_tar = self.local_program_tar  #远端压缩包路径


    def parse_conf(self,conf_file):
        #判断文件是否存在
        if not os.path.exists(conf_file):
            raise  Exception("{} not exist.".format(conf_file))

        required_keys = ['ips','password','ssh_port','user','trust_user']
        list_type_keys = ['ips','password']

        #判断文件是否是yaml文件，解析 yaml 文件
        with open(conf_file,'r',encoding='utf-8') as f:
            try:
                #conf 是字典
                conf = yaml.load(f.read(),Loader=yaml.FullLoader)
                #print(conf,type(conf))
            except Exception:
                raise Exception("{}: yaml file format err".format(conf_file))

        #判断文件中的 key 是否存在，并且是否都有值
        for k in required_keys:
            if k not in conf.keys():
                raise Exception("{} not in {}".format(k,conf_file))
            if conf[k] is None:
                raise Exception("invalid conf: {} should not be None".format(k))
        #获取 ip 的值切分成多个 ip，用 ，分隔的，每个值是一个字符串，放在列表中,判断ip是不是列表,判断 password 是不是列表
        for k in list_type_keys:
            #print(conf[k])
            #print(type(conf[k]))
            if not isinstance(conf[k],list):
                raise Exception('invalid conf: {}'.format(conf[k]))
            #conf[k] = [x.strip() for x in conf[k].split(',')]
            #print(conf[k])

        #判断 password 的长度是不是和 ips 的长度一致
        if len(conf['password']) != len(conf['ips']) :
            raise Exception('invalid conf:password is a list,bug not equal ips')

        #判断 ip 是否是合法的 ip
        for i in conf['ips']:
            if not check_ip(i):
                raise Exception('{} is not ip address.'.format(i))

        #检查端口是不是整数
        if not isinstance(conf['ssh_port'],int):
            raise Exception('ssh port must be digit,but now:{}'.format(conf['ssh_port']))

        #检查用户是不是正确的
        #conf['user'] = conf['user'] if 'user' in conf else os.environ.get('USER')
        #print(conf['user'])
        if conf['user'] != 'root':
            raise Exception('user must be root,current is {}'.format(conf['user']))

        #检查需要做免密的用户，如果没指定，使用当前用户
        #conf['trust_user']  = conf['trust_user'] if 'trust_user' in conf else os.environ.get('USER')
        #print(conf['trust_user'])

        #检查password,如果 password 不存在，设置为 '*****',密码的检查没有必要，前面有一个检查，如果密码不存在，或者值为空都会抛出异常
        #conf['password'] = conf['password'] if 'password' in conf else '*******'

        #初始化 conf.params   ip  port  username  password
        conf['ssh_params'] = dict()
        for ip in conf['ips']:
            conf['ssh_params'][ip] = {
                'host': ip,
                'port': conf['ssh_port'],
                'user': conf['user'],
                'password':conf['password'][conf['ips'].index(ip)]
            }

        with open(self.conf_json,'w',encoding='utf-8') as f:
            f.write(json.dumps(conf))

        return conf


    #检查提供的 ip 和密码是否能登录上
    def check_login(self):
        '''
        :检查ip是否能正常登录
        :return:
        '''
        for ip in self.conf['ips']:
            #password = self.conf['ssh_params'][ip]['password']
            cmd = "echo hello"
            ssh_client = SSHClient(**self.ssh_params[ip])
            login_res = ssh_client.check_paramiko(cmd)
            if not login_res[0]:
                raise Exception('paramiko login{}:{}'.format(self.ssh_params[ip],login_res))
            print('{}@{} logging success'.format(self.ssh_params[ip]['user'],self.ssh_params[ip]['host']))

    def copy_program_to_hosts(self):
        def copy_from_local(host,counters,lock):
            ssh_client = SSHClient(**self.ssh_params[host])
            if not host == self.ip:
                ssh_client.copy_from_local(self.local_program_tar,self.remote_program_tar,timeout=1800)



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('conf_file',help='config file')
    args = parser.parse_args()   #返回值是一个 Namespace 对象
    print(args)
    print(type(args))
    print(args.conf_file)


    main = Trust(args.conf_file)
    print(main.conf)
    main.check_login()

    #main.copy_program_to_hosts()



