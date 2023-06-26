'''
create_time: 2023/6/25 09:26
author: yss
version: 1.0
'''

#创建一个守护进程，每隔 1s 打印一次自己的 pid，主进程退出后观察守护进程的状态

import multiprocessing
import os
import time

def pr_func():  #后台进程运行的函数
    while True:
        print('i am child process,my pid is {}'.format(os.getpid()))
        time.sleep(1)




if __name__ == '__main__':
    p1 = multiprocessing.Process(target=pr_func,daemon=True)  #创建一个子进程并把它设置成守护进程
    p1.start()
    time.sleep(5)

