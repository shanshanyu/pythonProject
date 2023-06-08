'''
create_time: 2023/6/8 15:33
author: yss
version: 1.0
'''

import threading


def print_i():
    for i in range(100):
        print(threading.current_thread().name,i)

if __name__ == '__main__':
    t = threading.Thread(target=print_i,name='new_thread')  #创建线程对象
    t.start()  #启动线程

