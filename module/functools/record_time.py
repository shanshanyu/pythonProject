'''
create_time: 2024/8/5 14:59
author: yss
version: 1.0
desc: 创建一个装饰器函数，记录程序的执行时间
'''
import functools
import time


def record_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'exec spend {end-start} s')
    return wrapper


@record_time
def print_primer():
    '''
    打印 1~1000 里面的质数
    :return:
    '''
    for i in range(1,101):
        if i < 2:
            continue
        if i == 2 or i == 3:
            print(i)
            continue

        flag = True
        for j in range(2,int(i/2)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)


print_primer()


