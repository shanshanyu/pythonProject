'''
create_time: 2024/4/23 11:21
author: yss
version: 1.0

desc：下载文件，计算下载文件的时间  没有使用多线程或多进程
'''
import time
import random


def download_file(filename):
    print('开始下载',filename)
    time_sleep = random.randint(5,10)
    time.sleep(time_sleep)
    print(f'{filename}下载完成,耗时{time_sleep}s')


def main():
    start = time.time()
    download_file('西游记')
    download_file('水浒')
    end = time.time()

    print('下载耗时：%.2f s' % (end-start))


if __name__ == '__main__':
    main()
