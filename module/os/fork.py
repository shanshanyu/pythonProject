'''
create_time: 2023/6/17 14:32
author: yss
version: 1.0
'''

#创建一个子进程，子进程打印  我是子进程，父进程打印我是父进程

import os

pid = os.fork()
if pid == 0:
    print('我是子进程',os.getpid())
elif pid > 0:
    print('我是父进程，我的进程id是{},我的子进程id {}'.format(os.getpid(),pid))