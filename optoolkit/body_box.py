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
