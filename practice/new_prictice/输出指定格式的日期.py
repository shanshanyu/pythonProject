'''
使用 datetime 模块，输出日期
'''

import datetime

def main():
    input_date = input('请输入日期: ')
    new_date = datetime.date.fromisoformat(input_date)
    print(new_date.strftime('%Y/%m/%d'))



if __name__ == '__main__':
    main()