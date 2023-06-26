'''
create_time: 2023/6/21 18:39
author: yss
version: 1.0
'''

import psutil
print(psutil.cpu_times(),type(psutil.cpu_times()))  #返回 scputimes 对象

print(psutil.cpu_percent(interval=1,percpu=True))   #返回值是浮点数