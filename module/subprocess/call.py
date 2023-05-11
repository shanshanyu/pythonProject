'''
create_time: 2023/3/29 16:23
author: yss
version: 1.0
'''

import subprocess
subprocess.call("ls -l",shell=True)
subprocess.check_call("ls -l",shell=True)
a = subprocess.check_output("ls -l",shell=True,universal_newlines=True)
print(a)

b = subprocess.Popen("ls -l",shell=True,stdout=subprocess.PIPE)
print(b.stdout.read())