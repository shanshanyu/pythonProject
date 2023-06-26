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

#这是 flock 的正确用法，每个子进程调用一次 open，调用一次 flock



def print_num(queue):
    while True:
        #lock.acquire()  #加锁
        f = open('/tmp/process_sync', 'w')

        fcntl.flock(f,fcntl.LOCK_EX) #加锁
        print('hello')
        if queue.empty():
            #lock.release()
            fcntl.flock(f,fcntl.LOCK_UN)  #解锁
            print('list is empty')
            f.close()
            return
        num = queue.get()
        print('thread name={}'.format(multiprocessing.current_process().name),num,id(num))
        time.sleep(1)
        #lock.release()  #解锁
        fcntl.flock(f,fcntl.LOCK_UN)  #解锁


def get_num():
    q = multiprocessing.Queue()
    for i in range(20):
        q.put(i)

    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=print_num,args=(q,),name=str(i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()






if __name__ == '__main__':
    get_num()

