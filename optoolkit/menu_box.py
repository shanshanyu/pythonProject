'''
create_time: 2023/12/29 17:17
author: yss
version: 1.0
'''


import sys
import signal
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


    def title_box(self, title) :
        """
        title block
        """
        #设置标题
        if self.title_show:
            title_base = "\n" + self.offset + \
                         (len(self.pointer) + 1) * " " + "Main Menu"
            if title and isinstance(title, list):
                title_info = (
                        title_base + self.title_delimiter +
                        self.title_delimiter.join(title)
                )
            else:
                title_info = title_base

            result = self.color_style(
                title_info,
                mode="bold",
                background=self.background,
                font_color=self.title_color
            ) + "\n\n"
            #设置样式
            sys.stdout.write(result)
            sys.stdout.flush()

    def color_style(self,string, mode="", font_color="", background="") :
        """
        字体样式选择
        """
        styles = {
            "font_color" : {"black" : 30, "red" : 31, "green" : 32, "yellow" : 33,
                            "blue" : 34, "purple" : 35, "cyan" : 36, "white" : 37,
                            },
            "background" : {"black" : 40, "red" : 41, "green" : 42, "yellow" : 43,
                            "blue" : 44, "purple" : 45, "cyan" : 46, "white" : 47,
                            },
            "mode" : {"bold" : 1, "underline" : 4, "blink" : 5, "invert" : 7},
            "default" : {"end" : 0},
        }
        mode = str(styles["mode"].get(mode, ""))
        fore = str(styles["font_color"].get(font_color, ""))
        back = styles["background"].get(background, "")
        _end = styles["default"].get("end", 0)
        # 模式，字体，背景色
        _style = ";".join([s for s in [mode, fore, back] if s])
        style = f"\033[{_style}m"
        end = f"\033[{_end}m"
        return f"{style}{string}{end}"

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

    def help_box(self, content):
        """
        title block
        """
        if self.title_show:
            title_base = self.offset + \
                (len(self.pointer) + 1) * " " + "Usage"
            if content and isinstance(content, list):
                title_info = (
                    title_base + self.title_delimiter +
                    self.title_delimiter.join(content)
                )
            else:
                title_info = title_base

            result = self.color_style(
                title_info,
                background=self.background,
                font_color=self.help_color
            ) + "\n\n"
            sys.stdout.write(result)
            sys.stdout.flush()

    def body_box(self, pos, choose):
        """
        body block
        """
        i = 0
        result = ""
        while i < self.page_size:
            if i >= len(choose):
                result += "\r\n"
                i += 1
                continue

            content = str(choose[i][1])
            index = str(choose[i][0])

            if i == pos:
                line_content = (
                    index + ". " + content
                    if self.id_show
                    else content
                )
                temp = self.pointer + " " + line_content
                temp = self.color_style(
                    temp, background=self.background,
                    font_color=self.body_on_switch_color)
            else:
                line_content = (
                    index + ". " + content
                    if self.id_show
                    else content
                )
                temp = (len(self.pointer) + 1) * " " + line_content
                temp = self.color_style(
                    temp, background=self.background,
                    font_color=self.body_color)

            i += 1
            result += "\r" + self.offset + temp + "\n"

        sys.stdout.write(result)
        sys.stdout.flush()

    def foot_box(self, total, start, page):
        """
        foot block
        """
        result = ""
        next_page = False
        prev_page = False
        if self.foot_show:
            if start + self.page_size < total:
                next_page = True
            if start - self.page_size >= 0:
                prev_page = True

            foot = (
                "\n"
                + self.offset
                + (len(self.pointer) + 1) * " "
                + f"< {page} page / {total} tolal"
            )
            if next_page and prev_page:
                foot = foot + " Previous Next"
            elif next_page:
                foot = foot + " Next"
            elif prev_page:
                foot = foot + " Previous"
            foot += ">"
            result = result +\
                self.color_style(foot,
                                 background=self.background,
                                 font_color=self.foot_color) + "\n"

        sys.stdout.write(result)
        sys.stdout.flush()

    def get_pos(self) :
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

            try:
                # 返回一个匹配对象
                matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
                # 获取坐标
                groups = matches.groups()
                print(groups)
            except AttributeError:
                return 0, 0

            return int(groups[0]), int(groups[1])

        finally:
            termios.tcsetattr(stdin_fileno, termios.TCSANOW, old_tcattr)

    def menu_box(self, choose, pos, page_data, page, start,
                 title=None, guide=None):
        """
        展示整个选择菜单，原理清空屏幕后重新打印数据
        """
        self.clear_screen()
        total = len(choose)
        self.title_box(title)
        if guide:
            self.help_box(guide)
        self.body_box(pos, page_data)
        # self.foot_box(total, start, page)

    def draw(self,data, title=None, guide=None):
        """
            绘制表格
        """
        pos, start, page = 0, 0, 1
        page_size = self.page_size
        #如果title不是列表，把 title 转换成字符串放到列表中
        if title and isinstance(title, list) is False:
            title = [str(title)]
        if guide and isinstance(guide, list) is False:
            guide = [str(guide)]
        #把可迭代对象 data 变成索引序列
        data = [[i, v] for i, v in enumerate(data)]
        choose_list = data
        #按下 ctrl+c 后执行 menu_box
        signal.signal(signal.SIGINT, self.menu_box)

        while True:
            total = len(choose_list)
            if start + page_size < total:
                page_list = choose_list[start:start + page_size]
            else:
                page_list = choose_list[start:total]

            # 控制指针到达边界时
            if pos < 0:
                pos = len(page_list) - 1
            elif pos >= len(page_list):
                pos = 0

            self.menu_box(choose_list, pos, page_list,
                          page, start, title, guide)

if __name__ == '__main__':
    steps = [
        "Allinone Check",
        "Calculate Kudu Tserver Metadata Size",
        "Process Notify",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete",
        "Migration Evaluation",
        "Zookeeper_maxClientCnxns Change",
        "Change IP",
        "Fix docker0"
    ]
    m = Menu()
    pos = m.draw(steps, title="optoolkit",
                 guide="【Select】↑ ↓ 【choose】Enter 【Search】s/S 【Quit】q/Q/b/B\
    【Page】g/l")