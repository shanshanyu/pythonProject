'''
create_time: 2024/4/23 11:33
author: yss
version: 1.0

desc: 创建两个进程去下载文件  通过多进程的方式去下载文件
'''
import time
import random
import multiprocessing


def download_file(filename):
    print('开始下载',filename)
    time_sleep = random.randint(5,10)
    time.sleep(time_sleep)
    print(f'{filename}下载完成,耗时{time_sleep}s')


class MyProcess(multiprocessing.Process):
    def __init__(self,filename):
        super().__init__()
        self.filename = filename

    def run(self) -> None:
        download_file(self.filename)


def main():
    start = time.time()
    p = MyProcess('西游记')
    p.start()
    p1 = MyProcess('水浒')
    p1.start()

    p.join()
    p1.join()
    end = time.time()

    print('下载耗时: %f' % (end-start))


if __name__ == '__main__':
    main()

