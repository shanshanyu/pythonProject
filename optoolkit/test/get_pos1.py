# 2024/4/13  15:57
import termios
import sys
import tty
import re


def get_pos():
    stdin_fd = sys.stdin.fileno()
    #保留原来的属性
    save_termios = termios.tcgetattr(stdin_fd)

    try:
        tty.setcbreak(stdin_fd)
        sys.stdout.write('\033[6n')
        sys.stdout.flush()

        res = ''
        while True:
            char = sys.stdin.read(1)
            res += char
            if char == 'R':
                break
        pos = re.search(r'^\x1b\[(\d+);(\d+)R$',res)
        print(pos.groups())

    finally:
        termios.tcsetattr(stdin_fd,termios.TCSAFLUSH,save_termios)


def clear_screen():
    pos = int(get_pos())
    while pos > 0:
        sys.stdout.write('\033[K\033[1A')
        sys.stdout.flush()
        pos -= 1

def main():
    clear_screen()


if __name__ == '__main__':
    main()