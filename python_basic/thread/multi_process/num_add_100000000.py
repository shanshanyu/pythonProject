'''
create_time: 2024/4/23 17:01
author: yss
version: 1.0

desc: 100000000 累加和，通过多进程的方法实现，创建 8 个进程
'''
import time
import multiprocessing


def add_num(section,queue):
    res = 0
    for i in section:
        res += i
    queue.put(res)


def main():
    start = time.time()
    result_queue = multiprocessing.Queue()

    process_list = []

    num = 100000000
    res = 0
    full_list = list(range(1,num+1))
    index = 0
    for _ in range(8):  # 用 8 个进程去计算.把切表切成 8 份
        section = full_list[index:index+12500000]
        p = multiprocessing.Process(target=add_num,args=(section,result_queue))
        process_list.append(p)
        p.start()
        index += 12500000

    for p in process_list:
        p.join()

    while not result_queue.empty():  # 队列非空就一直取
        res += result_queue.get()

    print(res)
    end = time.time()
    print('耗时: %2.fs' % (end-start))


if __name__ == '__main__':
    main()

