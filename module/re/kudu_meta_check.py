'''
create_time: 2024/3/21 15:50
author: yss
version: 1.0
'''
import requests
import re
import os
import subprocess
from app.utils.logger import Logger
from app.products.base_products.checker.abstract_checker import AbstractChecker, format_check_result


class KuduMetaSizeChecker(AbstractChecker):
    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)

    def get_tserver_data_dir(self):
        response = requests.get('http://localhost:8050/varz')
        if response.status_code != 200:
            self.logger.error('kudu tserver 8050 can not reachable')
            return ''

        fs_data_dir = re.search(r'--fs_data_dirs=([^\n]+)', response.content.decode()).group(1)
        return fs_data_dir

    @format_check_result
    def check(self,params):
        #获取tserver路径
        fs_data_dir = self.get_tserver_data_dir()
        if not fs_data_dir:
            return {'code': -1,
             'data': {
                'kudu port check':
                'kudu 8050 port not alive'
             },
             'solution': 'kudu 8050 端口未监听，请检查kudu服务'
             }

        # 如果 kudu data dir 有多个目录，转换成列表
        fs_data_dir_lst = fs_data_dir.split(',')
        all_meta_size = 0
        for tmp_dir in fs_data_dir_lst :
            tmp_dir = os.path.join(tmp_dir,'data')
            sudo_cmd = ['sudo su -c "find %s/*.metadata -type f -exec du -c {} +|tail -1"' % tmp_dir]
            result = subprocess.run(sudo_cmd,capture_output=True,text=True,shell=True)
            all_meta_size += int(result.stdout.split()[0]) #单位为 k

        #把 k 转换成 g，再和 50g 比大小
        all_meta_size = all_meta_size
        if all_meta_size > 50:
            return {'code': -1,
                    'data': {
                        'kudu meta check':
                            f'kudu meta size 超过 50g,当前大小 {all_meta_size}G 需要 compact'
                    },
                    'solution' : '按照 kudu compact sop 文档优化'
                    }
        else:
            return {'code' : 1,
                    'data' : {
                        'kudu meta check' :
                            'kudu meta size normal'
                    },
                    'solution' : f'kudu meta size normal'
                    }








