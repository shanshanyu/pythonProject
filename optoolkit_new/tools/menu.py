# 2024/4/13  20:56
import sys
import re
import tty
import termios
import time


class Menu(object):
    def __init__(self):
        self.title_box_show = 1
        self.title_delimiter = ' > '
        self.offset = 8
        self.pointer = ' -> '
        self.is_id_show = 1
        self.start = 0  # 列表中的位置,第一页是0，第二页是page_size
        self.pos = 0  # 每页中的位置
        self.page_size = 10  # 页长

    def get_pos(self):
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

    def clear_screen(self):
        '''
        清屏
        :return:
        '''
        pos = self.get_pos()
        for _ in range(pos):
            sys.stdout.write('\033[K\033[1A')
            sys.stdout.flush()

    def color_style(self,content,foreground_color='',background_color='',font_style=''):
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

    def title_box(self,title):
        if self.title_box_show:
            title_base = "Main Menu" + self.title_delimiter+self.title_delimiter.join(title) if title else "Main Menu"
            title_info = (self.offset+len(self.pointer)) * ' ' + title_base
            print(title_info)

    def menu_box(self,choose,title,guide):
        self.clear_screen()
        self.title_box(title)
        self.body_box(choose)

    def body_box(self,choose):
        choose_list = choose[self.start:self.page_size]
        choose_list = enumerate(choose_list)

        for k,v in choose_list:
            if self.is_id_show:
                content = str(k) + '.' + v
            else:
                content = v

            if self.pos == k:
                content = self.offset * ' ' + self.pointer + content
            else:
                content = (self.offset+len(self.pointer)) * ' ' + content
            print(content)

    def draw(self,choose,title=None,guide=None):
        self.menu_box(choose,title,guide)


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
    m.draw(steps, title=['optoolkit', 'abc'], guide="【Select】↑ ↓ 【choose】Enter 【Search】s/S 【Quit】q/Q/b/B\
    【Page】g/l")

