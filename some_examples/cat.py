'''
create_time: 2024/2/2 23:15
author: yss
version: 1.0
实现linux 上 cat 的功能

主要分为有参数和没有参数两种场景

这个程序可能会出现哪些异常？
input读数据的时候可能会出现 EOFError


'''
import sys


def cat():
    '''如果没有参数,该怎么做
        直接在输出设备上打印输入
    '''
    if not sys.argv[1:]:
        while True:
            try:
                print(input())
            except EOFError:
                sys.exit()
    else:
        '''多个文件的读写应该只写一次'''
        for file in sys.argv[1:]:
            with open(file) as f:
                print(f.read(),end='')


if __name__ == '__main__':
    cat()