'''
create_time: 2024/4/23 10:46
author: yss
version: 1.0

desc: 使用fork创建进程
'''


import os


def main():
    pid = os.fork()
    if pid == 0:
        print('child process')
    else:
        print('father process')


if __name__ == '__main__':
    main()