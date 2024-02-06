'''
create_time: 2024/2/5 11:38
author: yss
version: 1.1

在上一个版本上加一些异常处理

在获取输入的时候，处理2个异常：
KeyboardInterrupt
EOFError

打印文件，读取文件的时候处理一个异常：
OSError
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
            except KeyboardInterrupt:
                sys.exit()
    else:
        '''多个文件的读写应该只写一次'''
        try:
            contents = [open(file,'r').read() for file in sys.argv[1:]]
        except OSError as e:
            print(f'error read file:{e}')
        for content in contents:
            sys.stdout.write(content)


if __name__ == '__main__':
    cat()