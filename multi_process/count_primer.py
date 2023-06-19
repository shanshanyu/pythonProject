'''
create_time: 2023/6/17 20:48
author: yss
version: 1.0
'''

#通过多进程的方式计算指定范围内的素数个数

import os
import multiprocessing


def get_prime(start,end):
    if start > end:  #如果提供的参数有问题，程序直接退出
        return -1

    for i in range(start,end+1):
        if i < 2:   #如果给出的数中不满足后续的计算图的，直接跳过
            continue

        flag = True
        j = 2
        while j <= int(i/2):  #这个等号就是为了 4 个数留，其他的数没有必要，其他的数不需要遍历到 i/2，因为如果满足 i/2，肯定也能被 2 整除
            if i % j == 0:
                flag = False
                break
            j += 1

        if flag:
            print(i)



if __name__ == '__main__':
    p1 = multiprocessing.Process(target=get_prime,args=(1,4))
    p1.start()



