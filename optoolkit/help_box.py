'''
create_time: 2023/12/29 18:25
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


if __name__ == '__main__':
    m = Menu()
    m.title_box(True)
    m.help_box('ehllo')