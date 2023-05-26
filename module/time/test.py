'''
create_time: 2023/5/11 15:34
author: yss
version: 1.0
'''

import time

print(time.gmtime(0))  #获取时间开始的点 epoch


print(time.gmtime()) #当前的 UTC时间

print(time.localtime()) #当前的时间


print(time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime()))

import os.path

print(os.path.abspath(__file__))


print(time.asctime())

print(time.time())  #返回的是 float 类型的时间戳


print(time.localtime(time.time()))