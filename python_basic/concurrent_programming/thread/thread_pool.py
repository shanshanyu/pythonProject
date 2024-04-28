'''
create_time: 2023/6/8 18:43
author: yss
version: 1.0
'''
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def print_i(num):
    for i in range(num):
        print(threading.current_thread().name,i)


pool = ThreadPoolExecutor(max_workers=2)  #创建包含2个线程的线程池


f = pool.submit(print_i,50)

while not f.done():
    time.sleep(2)