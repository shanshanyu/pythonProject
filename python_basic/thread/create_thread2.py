'''
create_time: 2024/4/22 15:09
author: yss
version: 1.0

desc: 通过 threading.Thread() 创建线程对象，调用线程对象的 start 方法
'''

import threading


def print_i(val):
    for i in range(1,val):
        print(threading.current_thread().name,i)


def main():
    t = threading.Thread(target=print_i,name='my_thread',args=(10,))
    t.start()


if __name__ == '__main__':
    main()