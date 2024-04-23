'''
create_time: 2024/4/23 14:44
author: yss
version: 1.0
'''
import time
import threading
import random


def download_file(filename):
    print('开始下载',filename)
    time_sleep = random.randint(5,10)
    time.sleep(time_sleep)
    print(f'{filename}下载完成,耗时{time_sleep}s')


def main():
    start = time.time() # 开始时间
    t1 = threading.Thread(target=download_file,args=('西游记',))
    t1.start()
    t2 = threading.Thread(target=download_file,args=('水浒',))
    t2.start()
    t1.join()
    t2.join()
    end = time.time()

    print('下载耗时: %.2f' % (end-start))


if __name__ == '__main__':
    main()

