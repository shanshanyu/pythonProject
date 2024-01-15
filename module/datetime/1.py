'''
create_time: 2023/5/31 09:55
author: yss
version: 1.0
'''
import time

'''
datetime 模块是一个 py 文件，包是一个文件夹，也是一种模块
datetime 模块有 2 个变量，MINYEAR   MAXYEAR

datetime 模块有 5 个类： date   time  datetime   timedelta   tzinfo   timezone

timezone 的父类是  tzinfo
datetime 的父类是 date



datetime.datetime 类有哪些方法：


strftime：date   time   datetime   都有这个方法，可以把对象转换成字符串
strptime:   datetime 的类方法，把字符串转换成对象   


date对象有一个类方法：
date.today()

'''

import datetime
from datetime import date

print(datetime.MINYEAR)  #1  date  datetime 对象允许的最小年份
print(datetime.MAXYEAR)  #9999   date  datetime 对象允许的最大年份
print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'),type(datetime.datetime.now()))


#date    datetime  time    datetime 模块包含这几个类

#print(datetime.timedelta.resolution)


print(date.today())  #获取今天的日期   date类的类方法
print(date.fromtimestamp(time.time()))


print(datetime.datetime)    #<class 'datetime.datetime'>
print(datetime.datetime.now()) #2024-01-11 14:31:28.898923
print(type(datetime.datetime.now().now()))

print(type(datetime.datetime.today()))


# dt_input = input('请输入开始日期(20200808)后按回车：')
# day = int(input('请输入间隔天数：'))
# dt = datetime.strptime(dt_input,'%Y%m%d')
#
# delta = timedelta(days=day)
# print(delta)
# dt = dt+delta
# print(dt)


#date 类型的对象都是简单型的

