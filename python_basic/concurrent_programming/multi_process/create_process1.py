'''
create_time: 2023/6/17 16:58
author: yss
version: 1.0
'''

import multiprocessing
import os


class MyProcess(multiprocessing.Process):

    def run(self):
        print('i am child process,my pid is {},my parent pid is {}'.format(os.getpid(),os.getppid()))


print('i am parent process,my pid is {}'.format(os.getpid()))
p = MyProcess()
p.start()