'''
create_time: 2024/7/4 14:29
author: yss
version: 1.0
desc: sysctl -a |grep pid_max 发现系统最大线程数 32768，用程序测试一下
'''
import threading
import time


def test():
    time.sleep(300)


def main():
    count = 0
    threads = []
    for _ in range(100000):
        t = threading.Thread(target=test)
        threads.append(t)
        t.start()
        count += 1
        print(count)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()