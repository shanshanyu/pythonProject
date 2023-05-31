'''
create_time: 2023/5/31 10:31
author: yss
version: 1.0
'''

#计算时间

from datetime import date,time,datetime,timedelta

def calc_date():
    #捕获输入异常
    try:
        start_date = input('请输入开始时间,例如（20200808):')
        if not start_date.isdigit() or len(start_date) != 8:
            raise Exception('开始时间格式错误')
        num = int(input('请输入间隔天数：'))
    except Exception as e:
        print(e)

    dt = datetime.strptime(start_date,'%Y%m%d')
    delta = timedelta(days=num)

    print('推算后的日期',(dt+delta).strftime('%Y-%m-%d'),type(dt+delta))


def day_to_date(day):
    return datetime.utcfromtimestamp(day*24*3600).strftime('%Y-%m-%d').split()[0]

def date_to_day():
    input_dt = input('请输入时间,例如（20200808):')
    dt = datetime.strptime(input_dt,'%Y%m%d')  #获得 datetime 对象
    dt_origin = datetime.utcfromtimestamp(0)
    return str(dt - dt_origin).split()[0]  #timedelta类型




if __name__ == '__main__':
    print(date.fromordinal(20))  #返回起始时间 1-1-1-1 加上 20 后的日期
    print(datetime.now(),type(datetime.now()))  #获取当前时间  datetime 类型
    print(datetime.today(),type(datetime.today()))
    print(datetime.fromtimestamp(15))  #1970-01-01 加上指定时间戳后的时间
    print(datetime.utcfromtimestamp(15))  # 1970-01-01 加上指定时间戳后的时间
    print(datetime.utcfromtimestamp(19000*24*3600).strftime('%Y-%m-%d').split()[0])

    #calc_date()
    print(day_to_date(19001))
    print(date_to_day())

