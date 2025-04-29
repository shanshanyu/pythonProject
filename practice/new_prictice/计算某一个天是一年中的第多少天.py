'''输入某年某月某日，判断这一天是这一年的第几天？'''

a_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #平年
b_year = [31,29,31,30,31,30,31,31,30,31,30,31]  #闰年


def count_day():
    days = 0
    year = int(input('输入年: '))
    month = int(input('输入月: '))
    day = int(input('输入日: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        for i in range(0,month-1):
            days += b_year[i]
    else:
        for i in range(0,month-1):
            days += a_year[i]
    days += day

    print(days)



if __name__ == '__main__':
    count_day()