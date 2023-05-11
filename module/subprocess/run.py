'''
create_time: 2023/3/29 15:46
author: yss
version: 1.0
'''

import subprocess
a = subprocess.run(['ls','-l'])
print(a)
#subprocess.run("ls -l",shell=True)

#subprocess.run("exit 1",shell=True,check=True)

