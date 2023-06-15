<<<<<<< HEAD
# 2023/6/7 20:12
import threading


def thread_func(*args,**args1):
    print(args,type(args))
    print(args1,type(args1))
    print('i am thread')
    for i in range(100):
        print(threading.current_thread().name,i)

t1 = threading.Thread(target=thread_func,args=(1,2,3),kwargs={'a':1,'b':2})  #使用 Thread类的构造器
t1.start()
for i in range(100):
    #print(threading.current_thread().getName(), i)   #getName deprecated
    print(threading.current_thread().name, i)
=======
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

>>>>>>> origin/master
