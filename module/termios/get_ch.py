'''
create_time: 2024/4/18 16:16
author: yss
version: 1.0

desc: 获得某个字符对应的ascii
'''

import sys
import tty
import termios


def main():
    stdin_fd = sys.stdin.fileno()
    old_termios = termios.tcgetattr(stdin_fd)

    try:
        tty.setraw(stdin_fd,termios.TCSANOW)
        while True:
            ch = sys.stdin.read(1)
            if ch == 'q':
                break
            sys.stdout.write(ch)
            sys.stdout.flush()
    finally:
        termios.tcsetattr(stdin_fd,termios.TCSAFLUSH,old_termios)






if __name__ == '__main__':
    main()
