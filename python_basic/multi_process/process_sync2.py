'''
create_time: 2023/6/25 21:43
author: yss
version: 1.0
'''
'''
create_time: 2023/6/25 13:27
author: yss
version: 1.0
'''
'''
create_time: 2023/6/25 13:01
author: yss
version: 1.0
'''

import multiprocessing
import fcntl
import time

#这个程序是正确的，多进程实现进程间通信，可以通过 multiprocessing.Queue结构+multiprocess.Lock()

#lock = multiprocessing.Lock()





def print_num(queue,f):
    while True:
        #lock.acquire()  #加锁


        fcntl.lockf(f,fcntl.LOCK_EX) #加锁
        print('hello')
        if queue.empty():
            #lock.release()
            fcntl.lockf(f,fcntl.LOCK_UN)  #解锁
            print('list is empty')
            f.close()
            return
        num = queue.get()
        print('thread name={}'.format(multiprocessing.current_process().name),num,id(num))
        time.sleep(1)
        #lock.release()  #解锁
        fcntl.lockf(f,fcntl.LOCK_UN)  #解锁


def get_num():
    q = multiprocessing.Queue()
    for i in range(20):
        q.put(i)

    processes = []

    f = open('/tmp/process_sync', 'w')

    for i in range(3):
        p = multiprocessing.Process(target=print_num,args=(q,f),name=str(i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()






if __name__ == '__main__':
    get_num()

