'''
create_time: 2024/4/9 17:14
author: yss
version: 1.0
desc: 主菜单
'''

import re
import sys
import termios
import tty


class Menu(object):
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
        :param id_show:   是否显示行数
        :param title_show:  # 是否显示标题
        :param foot_show:   # 是否显示页脚
        :param page_size:   # 每页显示多少条
        :param pointer:     # 设置指示器，默认(➔)
        :param title_color:
            'black','red','green','yellow','blue','purple','cyan','white'
        :param foot_color:
            'black', 'red','green','yellow','blue','purple','cyan','white'
        :param body_color:
            'black', 'red', 'green','yellow','blue','purple','cyan','white'
        :param body_on_switch_color:
        'black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'
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

    def color_style(self, string, mode="", font_color="", background=""):
        """
        字体样式选择
        """
        styles = {
            "font_color": {"black": 30, "red": 31, "green": 32, "yellow": 33,
                           "blue": 34, "purple": 35, "cyan": 36, "white": 37,
                           },
            "background": {"black": 40, "red": 41, "green": 42, "yellow": 43,
                           "blue": 44, "purple": 45, "cyan": 46, "white": 47,
                           },
            "mode": {"bold": 1, "underline": 4, "blink": 5, "invert": 7},
            "default": {"end": 0},
        }
        mode = str(styles["mode"].get(mode, ""))
        fore = str(styles["font_color"].get(font_color, ""))
        back = str(styles["background"].get(background, ""))
        _end = styles["default"].get("end", 0)
        # \033[参数1;参数2;参数3m   参数1样式，参数2字体颜色，参数3 背景色
        _style = ";".join([s for s in [mode, fore, back] if s])
        style = f"\033[{_style}m"
        end = f"\033[{_end}m"
        return f"{style}{string}{end}"

    def get_pos(self):
        '''
        获得当前光标位置
        :return:
        '''
        result = ""
        stdin_fileno = sys.stdin.fileno()
        old_setting = termios.tcgetattr(stdin_fileno)
        try:
            tty.setraw(stdin_fileno)
            sys.stdout.write('\033[6n')
            sys.stdout.flush()
            while True:
                '''
                这里可以简化一下，ch 的作用是追加到 result 上，可以直接把 sys.stdin.read(1) 的结果追加到 result 上
                减少了一个变量
                '''
                # ch = sys.stdin.read(1)
                # result += ch
                # if ch == 'R':
                #     break
                result += sys.stdin.read(1)
                if result[-1] == 'R':
                    break
        finally:
            termios.tcsetattr(stdin_fileno,termios.TCSADRAIN,old_setting)
        try:
            '''
            re.groups 如果 re 匹配对象为 None，那么调用 groups 方法会抛出异常 AttributeError
            '''
            match = re.match(r"\x1b\[(\d+);(\d+)R",result)
            group = match.groups()
        except AttributeError:
            return 0,0
        return int(group[0]),int(group[1])

    def clear_screen(self):
        '''
        获取当前光标的位置，然后回车清空内容，再退一行
        :return:
        '''
        self._term_end_pos = self.get_pos()[0]
        back_line = self._term_end_pos - self._term_start_pos
        for _ in range(back_line):
            sys.stdout.write('\r\033[K\033[A')
            sys.stdout.flush()

    def title_box(self,title):
        if self.title_show:
            #默认的title内容，如果title有值的话，再拼接
            title_base = '\n'+self.offset + (len(self.pointer)+1)*' ' + 'Main Menu'

            if title and isinstance(title,list):
                title_info = title_base + self.title_delimiter + self.title_delimiter.join(title)
            else:
                title_info = title_base  #如果 title 不是列表，或者不存在，不用打印 title 的内容

            result = self.color_style(
                title_info,
                mode='bold',
                font_color=self.title_color,
                background=self.background
                )+'\n\n'  #后面加两个换行
            sys.stdout.write(result)
            sys.stdout.flush()

    def help_box(self,guide):
        if self.title_show:  #help_box 和 title_box 公用一个开关
            help_base = self.offset + (len(self.pointer)+1)*' ' + 'Usage: '
            if guide and isinstance(guide,list):
                help_info = help_base + self.title_delimiter + self.title_delimiter.join(guide)
            result = self.color_style(
                    help_info,
                    font_color=self.help_color,
                    background=self.background
                    ) + '\n\n'
            print(result.encode('utf-8'))
            sys.stdout.write(result)
            sys.stdout.flush()

    def body_box(self,pos,choose):
        result = ''

        i = 0
       # while i < self.page_size:  #i 的判断条件应该和 page_size 对比，如果 choose 列表的内容少，后面应该打印换行回车
        while i < self.page_size:
            if i >= len(choose): #如果超过了列表的长度，但是没有达到 page_size，应该输出空行
                result += '\r\n'
                i += 1
                continue
            #这里要把 index 和 content 转换成字符串，不然后面拼接字符串会报错
            index = str(choose[i][0])
            content = str(choose[i][1])
            if i == pos:
                line_content = (index+'. '+content if self.id_show else content)
                temp = self.pointer + ' ' + line_content  #self.pointer 加个空格会不会好看点
                line_info = self.color_style(
                    temp,
                    font_color=self.body_on_switch_color,
                    background=self.background
                )
            else:
                line_content = (index+'. '+content if self.id_show else content)
                temp = (len(self.pointer)+1) * ' ' + line_content
                line_info = self.color_style(
                    temp,
                    font_color=self.body_color,
                    background=self.background
                )
            i += 1
            result += '\r' + self.offset + line_info + '\n'

        sys.stdout.write(result)
        sys.stdout.flush()

    def foot_box(self,total,start,page):
        '''
        页脚
        :param total: 总共的条目个数
        :param start: 每页的开始第一行索引
        :param page: 页数，初始化的时候是 1
        :return:
        '''
        result = ''
        next_page = False
        prev_page = False
        if self.foot_show:
            if start + self.page_size < total:
                next_page = True
            if start - self.page_size >= 0:
                prev_page = True

            foot = ('\n' + self.offset + (len(self.pointer)+1) * ' ' + f'< {page} page / {total} total')

            if next_page and prev_page:
                foot += ' Previous Next'
            elif next_page:
                foot += ' Next'
            elif prev_page:
                foot += ' Previous'

            foot += '>'

            result = self.color_style(
                foot,
                font_color=self.foot_color,
                background=self.background
            )+'\n\r'
            sys.stdout.write(result)
            sys.stdout.flush()

    def menu_box(self,choose,pos,page_data,page,start,title=None,guide=None):
        '''
        打印菜单
        :param choose: 所有的条目数据，格式是 [[index,content],[index,content]...]
        :param pos: pointer 的位置，在当前页的
        :param page_data: 当前页的内容
        :param page: 当前页的索引，从 1 开始
        :param start: 当前页的第一条数据的索引
        :param title:
        :param guide:
        :return:
        '''
        #清屏
        self.clear_screen()
        self.title_box(title)
        total = len(choose)
        #如果guide存在，再打印help_box
        if guide:
            self.help_box(guide)
        #body_box 需要当前的pos位置，和需要打印的数据
        self.body_box(pos,page_data)
        self.foot_box(total,start,page)

    def get_ch(self) :
        """
        获取键盘输入
        """
        _input = sys.stdin.fileno()
        old_settings = termios.tcgetattr(_input)
        try:
            #用 raw 模式获取键盘输入
            tty.setraw(sys.stdin.fileno())
            #tty.setcbreak(_input)
            choice = sys.stdin.read(1)
            if choice == "\x1b":
                choice += sys.stdin.read(2)
        finally:
            termios.tcsetattr(_input, termios.TCSADRAIN, old_settings)
        return choice

    def search_box(self,choose,title):
        '''
        展示搜索框，原理清空屏幕后重新打印数据
        :param choose:
        :param title:
        :return:
        '''
        self.clear_screen()
        search_title = title + ["Search"] if title else ["Search"]
        self.title_box(search_title)
        result = "\r\n" + self.offset + "key: "
        sys.stdout.write(result)
        sys.stdout.flush()
        keyword = sys.stdin.readline().strip()
        # filter 函数返回的是一个filter 对象，可以用list 转换成列表
        filter_choose = list(filter(lambda x: keyword in str(x[1]), choose))
        return filter_choose

    def draw(self,choose,title=None,guide=None):
        '''
        处理数据，然后传递给 menu_box
        :param choose: 是一个列表，转换成一个索引序列
        :param title:
        :param guide:
        :return:
        '''

        #pos 初始位置是 0，start 初始位置也是 0，page表示页数，初始是 1
        pos,start,page = 0,0,1
        page_size = self.page_size

        #如果 title 存在，但是不是列表，可以给转换成列表
        if title and isinstance(title,list) is False:
            title = [str(title)]
        if guide and isinstance(guide,list) is False:
            guide = [str(guide)]

        data = [[i, v] for i, v in enumerate(choose)]
        choose_list = data

        #signal 这个函数没有用，在 raw 模式下，contrl+c 识别不了,不会把他当成特殊按键，发送 sigint 信号
        #signal.signal(signal.SIGINT,xx)

        while True:
            total = len(choose_list)
            #获取 body_box 需要打印的内容，如果 start 所在的页
            if start + page_size < total:
                page_list = choose_list[start:start+page_size]
            else:
                page_list = choose_list[start:total]

            #指针到达边界
            if pos < 0:
                pos = len(page_list) - 1   #不应该用 start + page_size -1，这种在 page 满的情况下是没问题，没满就有问题
            if pos >= len(page_list):
                pos = 0

            #绘制菜单
            self.menu_box(choose_list,pos,page_list,page,start,title,guide)

            #获取键盘输入
            key = self.get_ch()
            #选中内容返回
            if key == '\r':
                #列表非空，防呆设计
                if len(choose_list) != 0:
                    #当前的 pos 位置
                    index = page_size * (page - 1) + pos
                    #获取选中的内容
                    return choose_list[index][0],choose_list[index][1]
            elif key in ["b", "B", "q", "Q"]:  # 返回
                return -1, None
            #下键，或者 k K
            elif key in ["\x1b[A", "k", "K"]:
                pos -= 1
            #上键，或者 j J
            elif key in ["\x1b[B", "j", "J"]:
                pos += 1
            elif key in ["\x1b[D", "h", "H"]:  # 上一页
                if start - page_size >= 0:
                    start -= page_size
                    pos = 0
                    page -= 1
            elif key in ["\x1b[C", "l", "L"]:  # 下一页
                if start + page_size < total:
                    start += page_size
                    pos = 0
                    page += 1
            elif key in ["S", "s"]:  # 搜索
                choose_list = self.search_box(choose_list,title)

            elif key in ["X", "x"]:  # 取消搜索
                choose_list = data


if __name__ == '__main__':
    m = Menu()
    # m.clear_screen()
    # m.title_box(None)
    # m.help_box(['1','2','3'])
    # m.body_box(0,[['1','2'],['3','4']])
    # m.foot_box(15,0,1)
    # m.menu_box([['1','2'],['3','4']],0,[['1','2'],['3','4']],1,0)
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
    res = m.draw(steps)
    print(res)
