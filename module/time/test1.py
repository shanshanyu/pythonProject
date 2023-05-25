'''
create_time: 2023/5/24 15:57
author: yss
version: 1.0
'''

import time
#print(time.time())

print(time.localtime())

print(time.gmtime())


print(time.strftime("%Y%m%d %H:%M:%S",time.localtime(time.time())))