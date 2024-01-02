'''
create_time: 2023/12/29 17:01
author: yss
version: 1.0
'''

import sys
import termios
import tty
import re


class Menu(object):
    """
    命令行菜单
    """
    def __init__(self):

        self._term_start_pos = 0
        self._term_end_pos = 0
        self.offset = " " * 8  # 菜单距离左侧偏移量
        self.id_show = True  # 是否显示列表id
        self.title_show = True  # 标题是否显示
        self.foot_show = True  # 页脚是否显示
        self.page_size = 10  # 每页显示多少条
        self.title_delimiter = " > "  # 定义标题分隔符
        self.pointer = "➔ "  # 定义选择指示器
        self.background = ""   # 背景颜色
        self.title_color = "purple"
        self.help_color = "blue"
        self.foot_color = "yellow"
        self.body_color = "white"
        self.body_on_switch_color = "green"

    def get_pos(self):
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
            # stdout 把指令发给了显示器，显示器返回给标准输入
            sys.stdout.write("\x1b[6n")
            sys.stdout.flush()

            while True :
                buf += sys.stdin.read(1)
                if buf[-1] == "R" :
                    break

            try :
                # 返回一个匹配对象
                matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
                # 获取坐标
                groups = matches.groups()
                print(groups)
            except AttributeError :
                return 0, 0

            return int(groups[0]), int(groups[1])

        finally :
            termios.tcsetattr(stdin_fileno, termios.TCSANOW, old_tcattr)

    def clear_screen(self) :
        """
        清理屏幕, 根据开始行和结束行，计算回退行数
        """
        self._term_end_pos = self.get_pos()[0]
        back_line = self._term_end_pos - self._term_start_pos
        for _ in range(back_line) :
            # \r' 转义字符,回到行首
            #sys.stdout.write("\r\033[K\033[1A")
            #\r 回到行首
            #\033[K 清除光标到行尾的内容
            #\033[1A 回到上一行
            sys.stdout.write("\r\x1b[K\033[1A")
            sys.stdout.flush()


if __name__ == '__main__':
    m = Menu()
    m.clear_screen()


