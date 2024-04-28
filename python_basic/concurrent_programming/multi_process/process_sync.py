'''
create_time: 2023/6/25 13:01
author: yss
version: 1.0
'''
import fcntl
import multiprocessing
import sys

#多进程中的进程同步能否通过全局变量来实现
#不能，每个进程有独立的副本

#这个程序是错误的，因为用了全局变量来做进程间同步

file_lst = []

#f = open('/tmp/test','w')
#fno = f.fileno()
lock = multiprocessing.Lock()
def print_num():
    while True:
        #fcntl.lockf(fno,fcntl.LOCK_EX) #加锁
        lock.acquire()
        global file_lst
        print(file_lst)
        if len(file_lst) == 0:
            #fcntl.lockf(fno,fcntl.LOCK_UN)  #解锁
            lock.release()
            print('list is empty')
            return
        num = file_lst.pop()
        print(num,id(num))
        print(file_lst,id(file_lst))
        #fcntl.lockf(fno,fcntl.LOCK_UN)  #解锁
        lock.release()


def get_num():
    global file_lst
    for i in range(5):
        file_lst.append(i)

    for i in range(3):
        p = multiprocessing.Process(target=print_num)
        p.start()




if __name__ == '__main__':
    get_num()
    #f.close()
