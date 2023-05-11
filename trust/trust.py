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
from env_utils import check_ip


sys.argv.append('test.yml')
print(sys.argv)

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
print(WORK_DIR)

class Trust(object):
    def __init__(self,conf_file):
        self.conf_json = os.path.join(WORK_DIR,'trust.json')
        self.conf = self.parse_conf(conf_file)

    def parse_conf(self,conf_file):
        #判断文件是否存在
        if not os.path.exists(conf_file):
            raise  Exception("{} not exist.".format(conf_file))

        required_keys = ['ips','password','ssh_port']
        list_type_keys = ['ips']

        #判断文件是否是yaml文件，解析 yaml 文件
        with open(conf_file,'r',encoding='utf-8') as f:
            try:
                #conf 是字典
                conf = yaml.load(f.read(),Loader=yaml.FullLoader)
                print(conf)
            except Exception:
                raise Exception("{}: yaml file format err".format(conf_file))

        #判断文件中的 key 是否存在，并且是否都有值
        for k in required_keys:
            if k not in conf.keys():
                raise Exception("{} not in {}".format(k,conf_file))
            if conf[k] is None:
                raise Exception("invalid conf: {} should not be None".format(k))
        #获取 ip 的值切分成多个 ip，用 ，分隔的，每个值是一个字符串，放在列表中,判断ip是不是列表
        for k in list_type_keys:
            #print(conf[k])
            #print(type(conf[k]))
            if not isinstance(conf[k],list):
                raise Exception('invalid conf: {}'.format(conf[k]))
            #conf[k] = [x.strip() for x in conf[k].split(',')]
            #print(conf[k])
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

        #检查需要做免密的用户
        conf['trust_user']  = conf['trust_user'] if 'trust_user' in conf else os.environ.get('USER')
        print(conf['trust_user'])

        #检查password,如果 password 不存在，设置为 '*****',密码的检查没有必要，前面有一个检查，如果密码不存在，或者值为空都会抛出异常
        #conf['password'] = conf['password'] if 'password' in conf else '*******'
        #password的长度需要和 ip 的长度保持一致
        if isinstance(conf['password'],list):
            if len(conf['password']) != len(conf['ips']):
                raise Exception('invalid conf:password is a list,bug not equal ips')


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
        for ip in self.







if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('conf_file',help='config file')
    args = parser.parse_args()
    print(args)
    print(type(args))
    print(args.conf_file)
    main = Trust(args.conf_file)
    print(main.conf)



