'''
create_time: 2023/6/17 14:44
author: yss
version: 1.0
'''

#创建三个子进程，每个子进程用二分查找查找一个整数

import multiprocessing
import time

#创建多个进程二分查找一个数

lst = []

for i in range(300):
    lst.append(i)
def bin_search(lst,length,num):
    print(f'{multiprocessing.Process().name} running')
    if num < lst[0] or num > lst[length-1]:
        return -1


    high = length - 1
    low = 0

    while low <= high:
        mid = int((high+low)/2)

        if lst[mid] < num:
            low = mid+1
        elif lst[mid] > num:
            high = mid-1
        else:
            print(lst[mid])
            return 0

    return -1


#创建 3 个进程来找数

if __name__ == '__main__':
    num = 295
    one_third_len = int(len(lst)/3)
    p1 = multiprocessing.Process(target=bin_search,args=(lst[:int(len(lst)/3)],one_third_len,num),name='p1')
    p2 = multiprocessing.Process(target=bin_search,args=(lst[int(len(lst)/3):int(len(lst)/3*2)],one_third_len,num),name='p2')
    p3 = multiprocessing.Process(target=bin_search,args=(lst[int(len(lst)/3*2):],one_third_len,num),name='p3')

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


