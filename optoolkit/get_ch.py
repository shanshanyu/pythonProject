'''
create_time: 2024/1/2 21:37
author: yss
version: 1.0
'''

import sys
import termios
import tty

def get_ch() :
    """
    获取键盘输入
    """
    _input = sys.stdin.fileno()
    old_settings = termios.tcgetattr(_input)
    try:
        tty.setraw(sys.stdin.fileno())
        choice = sys.stdin.read(1)
        if choice == "\x1b":
            choice += sys.stdin.read(2)
    finally:
        termios.tcsetattr(_input, termios.TCSADRAIN, old_settings)
    return choice

if __name__ == '__main__':
    ch = get_ch()
    print(ch.encode())