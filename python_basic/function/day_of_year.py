'''
create_time: 2024/3/7 15:17
author: yss
desc: 获取某个日期是1年中的第多少天
version: 1.0


输入年月日->判断是否是闰年->把每个月份的天数加起来(平年和闰年有区别）->返回天数
'''

def is_leap_year(year):
    if year%4 == 0 and year%100 !=0 or year%400 == 0:
        return True
    else:
        return False


def day_of_year(year,month,day):
    if is_leap_year(year):
        day_of_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    count = 0
    for i in range(month-1):  #如果输入 8 应该是1~7月再加上8月的天数
        count += day_of_month[i]

    count += day
    return count


if __name__ == '__main__':
    day = day_of_year(2001,3,1)
    print(day)