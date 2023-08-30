'''
create_time: 2023/8/30 17:30
author: yss
version: 1.0
输入年份判断是不是闰年
'''

year = int(input('请输入年份： '))

if ((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0):
    print('%d 是闰年' % year)
else:
    print('%d 不是润年' % year)