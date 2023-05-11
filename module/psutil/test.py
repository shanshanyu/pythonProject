'''
create_time: 2023/5/11 15:21
author: yss
version: 1.0
'''

import psutil

print(psutil.cpu_count(logical=False))  #cpu个数

#print(psutil.cpu_percent(1,True)) #cpu使用率

mem = psutil.virtual_memory()  #查看内存信息
print(mem)
print(mem.total)  #查看内存的总大小

disk = psutil.disk_partitions()  #查看磁盘的分区
print(disk)
print(psutil.disk_usage('/'))  #查看磁盘使用率

print(psutil.net_if_addrs())  #查看网卡信息

print(psutil.users())  #查看当前登录的用户