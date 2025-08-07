import sys
import time

def record_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print('程序运行 %.1f' % (end_time - start_time))
        return ret
    return wrapper


@record_time
def download(filename):
    print(f'开始下载文件{filename}')
    time.sleep(6)
    print(f'下载完成{filename}')



if __name__ == '__main__':
    download('哈利波特')
