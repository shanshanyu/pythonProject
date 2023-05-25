'''
create_time: 2023/5/17 14:55
author: yss
version: 1.0
'''

import time
import psutil

now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(now_time)

print("物理cpu核数",psutil.cpu_count(logical=False))
print("逻辑cpu核数",psutil.cpu_count(logical=True))


#print(psutil.cpu_percent(1))  #查看 1s 内的 cpu 使用率

#内存信息

total = round(psutil.virtual_memory().total/(1024*1024*1024))
print(psutil.virtual_memory())
free = round(psutil.virtual_memory().available/(1024*1024*1024))
print("总共有 {} G".format(total))
print("剩余 {} G".format(free))

print(time.localtime(psutil.boot_time()))