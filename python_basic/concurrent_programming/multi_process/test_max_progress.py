'''
Data: 2024/7/9 21:58
Author: yss
Desc: 测试用户支持多少个进程,应该受 pid_max  nproc的限制
'''
import multiprocessing
import os
import time


def test():
    time.sleep(300)
    os.getpid()


def main():
    count = 0
    for i in range(1000000):
        p = multiprocessing.Process(target=test)
        p.start()
        count += 1
        print(count)


if __name__ == '__main__':
    main()