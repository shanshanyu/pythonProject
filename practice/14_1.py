'''
create_time: 2023/5/31 09:53
author: yss
version: 1.0
'''
from datetime import date,time,datetime,timedelta

#输出几天后的日期  用 datetime + timedelta，  datetime 通过 datetime.strptime 来获取
print(date.today())  #获取今天的日期
print(datetime.today())  #获取当前时间 时区为None
print(datetime.now()) #获取当前时间  可以指定时区
print(datetime.utcnow())  #获取当前时间  utc时区


dt_input = input('请输入开始日期(20200808)后按回车：')
day = int(input('请输入间隔天数：'))

dt = datetime.strptime(dt_input,'%Y%m%d')
dt = dt + timedelta(days=day)
print(dt)