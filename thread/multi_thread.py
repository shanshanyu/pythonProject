'''
create_time: 2023/6/14 15:57
author: yss
version: 1.0
'''
import threading


#创建多个线程，每个线程对 1 个数加 10 00000，然后打印加完后的值


num = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        global mutex
        with mutex:
            for i in range(1000000):
                num += 1
            print(num)


thread_list = []

for i in range(5):
    t = MyThread()
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()


