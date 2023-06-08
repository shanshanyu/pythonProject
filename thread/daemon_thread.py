'''
create_time: 2023/6/8 17:50
author: yss
version: 1.0
'''
import threading
import time


def traversal(num):
    for i in range(num):
        print(threading.current_thread().name,i)


t = threading.Thread(target=traversal,args=(100,),daemon=True)
t.start()

print('hello')  #前台线程结束，后台线程也随之结束

