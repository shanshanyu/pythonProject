'''
create_time: 2023/5/31 09:55
author: yss
version: 1.0
'''
from datetime import datetime,time,timedelta,date
#print(datetime.MINYEAR)  #1  date  datetime 对象允许的最小年份
#print(datetime.MAXYEAR)  #9999   date  datetime 对象允许的最大年份

#date    datetime  time    datetime 模块包含这几个类

#print(datetime.timedelta.resolution)


print(date.today())  #获取今天的日期


dt_input = input('请输入开始日期(20200808)后按回车：')
day = int(input('请输入间隔天数：'))
dt = datetime.strptime(dt_input,'%Y%m%d')

delta = timedelta(days=day)
print(delta)
dt = dt+delta
print(dt)


#date 类型的对象都是简单型的

