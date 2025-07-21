'''输入一个 1582 年以后的年份，判断该年份是不是闰年'''

year = int(input('请输入年份：'))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('闰年')
else:
    print('不是闰年')