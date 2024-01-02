'''
create_time: 2023/12/29 15:30
author: yss
version: 1.0
'''

import sys
import termios
import tty
import re

def get_pos():
    """
    获取当前光标位置
    """
    buf = ""
    # 获取标准输入文件描述符
    stdin_fileno = sys.stdin.fileno()
    #
    old_tcattr = termios.tcgetattr(stdin_fileno)

    try:
        tty.setcbreak(stdin_fileno, termios.TCSANOW)
        #stdout 把指令发给了显示器，显示器返回给标准输入
        sys.stdout.write("\x1b[6n")
        sys.stdout.flush()

        while True:
            buf += sys.stdin.read(1)
            if buf[-1] == "R":
                break

        try:
            #返回一个匹配对象
            matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
            #获取坐标
            groups = matches.groups()
            print(groups)
        except AttributeError:
            return 0, 0

        return int(groups[0]), int(groups[1])

    finally:
        termios.tcsetattr(stdin_fileno, termios.TCSANOW, old_tcattr)






if __name__ == '__main__':
    get_pos()
