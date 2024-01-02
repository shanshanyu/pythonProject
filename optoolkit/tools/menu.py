'''
create_time: 2023/12/29 10:27
author: yss
version: 1.0
'''

import signal
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
        self.background = ""  # 背景颜色
        self.title_color = "purple"
        self.help_color = "blue"
        self.foot_color = "yellow"
        self.body_color = "white"
        self.body_on_switch_color = "green"

    def style(
            self,
            id_show=True,
            title_show=True,
            foot_show=True,
            page_size=10,
            pointer="➔ ",
            title_color="purple",
            help_color="blue",
            foot_color="yellow",
            body_color="white",
            body_on_switch_color="green",
    ):
        """
        菜单样式设置
        供选择的颜色：'black', 'red', 'green', 'yellow',
                    'blue', 'purple', 'cyan', 'white'
        :param id_show: 是否显示行数
        :param title_show: 是否显示标题
        :param foot_show:  是否显示页脚
        :param page_size:  每页显示多少条
        :param pointer:  设置指示器，默认(➔)
        :param title_color: black','red','green','yellow','blue','purple','cyan','white'
        :param help_color: black','red','green','yellow','blue','purple','cyan','white'
        :param foot_color: black','red','green','yellow','blue','purple','cyan','white'
        :param body_color: black','red','green','yellow','blue','purple','cyan','white'
        :param body_on_switch_color: black','red','green','yellow','blue','purple','cyan','white'
        :return:
        """
        self.id_show = id_show  # 是否显示列表id
        self.title_show = title_show  # 标题是否显示
        self.foot_show = foot_show  # 页脚是否显示
        self.page_size = page_size  # 每页显示多少条
        self.pointer = pointer  # 定义选择指示器
        self.title_color = title_color  # 标题颜色
        self.help_color = help_color  # 帮助颜色
        self.foot_color = foot_color  # 页脚颜色
        self.body_color = body_color  # 主体文字颜色
        self.body_on_switch_color = body_on_switch_color  # 选择的主体文字颜色

    def get_pos(self):
        """
        获取当前光标位置
        """
        buf = ""
        stdin = sys.stdin.fileno()
        tattr = termios.tcgetattr(stdin)

        try:
            tty.setcbreak(stdin, termios.TCSANOW)
            sys.stdout.write("\x1b[6n")
            sys.stdout.flush()

            while True:
                buf += sys.stdin.read(1)
                if buf[-1] == "R":
                    break
        finally:
            termios.tcsetattr(stdin, termios.TCSANOW, tattr)

        try:
            matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
            groups = matches.groups()
        except AttributeError:
            return 0, 0

        return int(groups[0]), int(groups[1])

    def clear_screen(self):
        """
        清理屏幕, 根据开始行和结束行，计算回退行数
        """
        self._term_end_pos = self.get_pos()[0]
        back_line = self._term_end_pos - self._term_start_pos
        for _ in range(back_line):
            # \r' 转义字符,回到行首
            sys.stdout.write("\r\033[K\033[1A")
            sys.stdout.flush()

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
        self.foot_box(total, start, page)

    def draw(self,data, title=None, guide=None):
        """
            绘制表格
        """
        pos, start, page = 0, 0, 1
        page_size = self.page_size

        if title and isinstance(title, list) is False :
            title = [str(title)]
        if guide and isinstance(guide, list) is False :
            guide = [str(guide)]
        data = [[i, v] for i, v in enumerate(data)]
        choose_list = data

        signal.signal(signal.SIGINT, self.menu_box)

        while True:
            total = len(choose_list)
            if start + page_size < total :
                page_list = choose_list[start : start + page_size]
            else :
                page_list = choose_list[start :total]

            # 控制指针到达边界时
            if pos < 0:
                pos = len(page_list) - 1
            elif pos >= len(page_list) :
                pos = 0

            self.menu_box(choose_list, pos, page_list,
                          page, start, title, guide)

            key = self.get_ch()
            if key == "\r":  # enter
                if len(choose_list) != 0 :
                    ids = page_size * (page - 1) + pos
                    return choose_list[ids][0], choose_list[ids][1]

            elif key in ["b", "B", "q", "Q"] :  # 返回
                return -1, None

            elif key in ["\x1b[A", "k", "K"] :
                pos -= 1

            elif key in ["\x1b[B", "j", "J"] :
                pos += 1

            elif key in ["\x1b[D", "h", "H"] :  # 上一页
                if start - page_size >= 0 :
                    pos = 0
                    start = start - page_size
                    page -= 1

            elif key in ["\x1b[C", "l", "L"] :  # 下一页
                if start + page_size < total :
                    pos = 0
                    start = start + page_size
                    page += 1

            elif key in ["S", "s"] :  # 搜索
                choose_list = self.search_box(choose_list, title)

            elif key in ["X", "x"] :  # 取消搜索
                choose_list = data

'''
create_time: 2023/12/29 18:37
author: yss
version: 1.0
'''

import sys


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

    def body_box(self, pos, choose):
        """
        body block
        """
        i = 0
        result = ""
        while i < self.page_size:
            if i >= len(choose) :
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

    def draw(self,data,title=None,guide=None):
        start,pos,page = 0,0,1
        page_size = self.page_size
        data = [[i, v] for i, v in enumerate(data)]
        choose_list = data

        total = len(choose_list)
        if start + page_size < total:
            page_list = choose_list[start:start + page_size]
        else:
            page_list = choose_list[start:total]

        print(page_list)

        self.body_box(0, page_list)


if __name__ == '__main__':
    m = Menu()
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
        "Fix docker0",
        "test1",
        "test2"
    ]
    m.draw(steps, title="optoolkit",
                 guide="【Select】↑ ↓ 【choose】Enter 【Search】s/S 【Quit】q/Q/b/B\
【Page】g/l")
