'''
create_time: 2024/4/1 11:04
author: yss
version: 1.0
'''

import subprocess



res = subprocess.check_output('ls -l',shell=True,stderr=subprocess.STDOUT)
print(res.decode('utf-8'))
