'''
create_time: 2023/12/29 11:30
author: yss
version: 1.0
'''

import sys
import termios
import tty

def main():
    #获取标准输入的文件描述符
    stdin_fileno = sys.stdin.fileno()
    #获取tty属性列表
    old_settting = termios.tcgetattr(stdin_fileno)
    print(old_settting)
    #设置tty为raw模式
    tty.setraw(stdin_fileno)
    for _ in range(5):
        char = sys.stdin.read(1)
        print(char)

    #还原tty属性
    termios.tcsetattr(stdin_fileno,termios.TCSADRAIN,old_settting)


if __name__ == '__main__':
    main()