# 2024/4/13  20:56
import sys
import re
import time
import tty
import termios


class Menu(object):
    def __init__(self):
        self.title_delimiter = ' > '
        self.offset = 8 * ' '
        self.pointer = ' -> '

        self.id_show = True
        self.title_show = True
        self.help_show = True
        self.foot_show = True

        self.start = 0  # 列表中的位置,第一页是0，第二页是page_size
        self.pos = 0  # 每页中的位置
        self.page_size = 10  # 页长
        self.page_index = 1  # 当前页

        self.title_color = 'purple'
        self.help_color = 'blue'
        self.body_color = 'white'
        self.body_on_switched_color = 'green'
        self.foot_color = 'yellow'
        self.background_color = ''

    @staticmethod
    def get_ch():
        '''
        使用cbreak模式，关闭回显
        :return:
        '''
        stdin_fd = sys.stdin.fileno()
        old_termios = termios.tcgetattr(stdin_fd)

        try:
            tty.setraw(stdin_fd, termios.TCSANOW)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch += sys.stdin.read(2)
            return ch

        finally:
            termios.tcsetattr(stdin_fd, termios.TCSAFLUSH, old_termios)

    @staticmethod
    def get_pos():
        '''
        获取光标位置
        :return:
        '''
        res = ''
        stdin_fd = sys.stdin.fileno()
        # 保存原来的 termios 信息
        old_termios = termios.tcgetattr(stdin_fd)

        try:
            # 丢弃缓冲区的数据，立即切换
            tty.setcbreak(stdin_fd,termios.TCSANOW)
            # 获取光标位置
            sys.stdout.write('\033[6n')
            sys.stdout.flush()

            while True:
                ch = sys.stdin.read(1)
                res += ch
                if ch == 'R':
                    break
        finally:
            termios.tcsetattr(stdin_fd,termios.TCSAFLUSH,old_termios)

        match = re.search(r'(\d+);(\d+)R$', res)
        return int(match.group(1))

    @staticmethod
    def clear_screen():
        '''
        清屏
        :return:
        '''
        pos = Menu.get_pos()
        for _ in range(pos):
            sys.stdout.write('\033[K\033[1A')
            sys.stdout.flush()

    @staticmethod
    def color_style(content,foreground_color='',background_color='',font_style=''):
        '''
        输入content，把content设置样式后返回
        :param content:
        :param color:
        :return:
        '''
        foreground = {'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,'dark_green':36,'white':37}
        background = {'black':40,'red':41,'green':42,'yellow':43,'blue':44,'purple':45,'dark_green':46,'white':47}
        style = {'highlight':1,'underline':4,'blink':5,'invert':7}
        foreground_color = foreground.get(foreground_color,'')
        background_color = background.get(background_color,'')
        font_style = style.get(font_style,'')

        return f'\033[{font_style};{foreground_color};{background_color}m{content}\033[0m'

    def help_box(self,guide):
        if self.help_show and guide:
            help_base = guide
            help_base = self.offset + len(self.pointer) * ' ' + help_base
            res = Menu.color_style(help_base,self.help_color,self.background_color,'highlight') + '\n\n'
            sys.stdout.write(res)
            sys.stdout.flush()

    def title_box(self,title):
        if self.title_show:
            if title and isinstance(title,list):
                title_base = "Main Menu" + self.title_delimiter + self.title_delimiter.join(title)
            else:
                title_base = "Main Menu"

            title_base = '\n' + self.offset + (len(self.pointer)+1) * ' ' + title_base
            res = Menu.color_style(title_base,self.title_color,self.background_color,'highlight') + '\n\n'
            sys.stdout.write(res)
            sys.stdout.flush()

    def menu_box(self,choose_list,page_list,title,guide):
        '''
        :param choose_list: 总数据
        :param page_list: 页数据
        :param title:
        :param guide:
        :return:
        '''
        Menu.clear_screen()
        self.title_box(title)
        self.help_box(guide)
        self.body_box(page_list)
        self.foot_box(choose_list)

    def body_box(self,choose):
        res = ''  # 所有的打印内容
        i = 0
        while i < self.page_size:
            if i >= len(choose):
                res += '\n'
                i += 1
                continue

            index = str(choose[i][0])
            content = str(choose[i][1])

            # 判断 id 是否显示
            line_content = index + '.' + content if self.id_show else content

            # 是否选中,选中会增加 pointer,增加颜色
            if self.pos == i:
                line_content = self.pointer + line_content
                line_content = Menu.color_style(line_content, self.body_on_switched_color, self.background_color, '')
            else:
                line_content = len(self.pointer) * ' ' + line_content
                line_content = Menu.color_style(line_content, self.body_color, self.background_color, '')

            line_content = self.offset + line_content + '\n'

            res += line_content
            i += 1

        sys.stdout.write(res)
        sys.stdout.flush()

    def foot_box(self,choose):
        next_page = False
        pre_page = False
        total = len(choose)
        if self.foot_show:
            if self.start + self.page_size < total:
                next_page = True

            if self.start - self.page_size >= 0:
                pre_page = True

            prefix = 'Previous' if pre_page else ''
            suffix = 'Next' if next_page else ''

            foot_base = f'< {self.page_index} page / {total} tolal {prefix} {suffix}>'
            foot_base = '\n' + self.offset + len(self.pointer) * ' ' + foot_base + '\n'
            res = Menu.color_style(foot_base,self.foot_color,self.background_color,'')
            sys.stdout.write(res)
            sys.stdout.flush()

    def draw(self,choose,title=None,guide=None):
        choose_list = list(enumerate(choose))
        total = len(choose_list)

        # title  guide 不是列表转换成列表
        if title and not isinstance(title,list):
            title = [str(title)]

        while True:
            page_list = choose_list[self.start:self.start+self.page_size] if self.start+self.page_size < total \
                else choose_list[self.start:total]

            self.menu_box(choose_list, page_list,title, guide)

            # 获取键盘输入
            ch = Menu.get_ch()

            # end = self.page_size-1 if self.start + self.page_size < total else total - self.start - 1
            # 上面的步骤就是计算页长

            if ch == '\r':
                index = self.start + self.pos
                return choose_list[index][0],choose_list[index][1]
            elif ch == 'q' or ch == 'Q':
                return -1,None
            elif ch == '\x1b[B':  # 下
                self.pos += 1
                if self.pos >= len(page_list):
                    self.pos = 0
            elif ch == '\x1b[A':  # 上
                self.pos -= 1
                if self.pos < 0:
                    self.pos = len(page_list)-1
            elif ch == '\x1b[D':   # 左
                if self.start - self.page_size >= 0:
                    self.page_index -= 1
                    self.start -= self.page_size
                    self.pos = 0
            elif ch == '\x1b[C':   # 右
                if self.start + self.page_size < total:
                    self.page_index += 1
                    self.start += self.page_size
                    self.pos = 0


if __name__ == '__main__':
    m = Menu()
    steps = [
        "Allinone Check",
        "Calculate Kudu Tserver Metadata Size",
        "Process Notify",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete",
        "Auto Event Delete",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete",
        "Auto Event Delete",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete"
    ]
    m.draw(steps, title='optoolkit_new', guide="【Select】↑ ↓ 【choose】Enter 【Quit】q/Q")

