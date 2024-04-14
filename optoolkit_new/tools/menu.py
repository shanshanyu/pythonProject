# 2024/4/13  20:56


class Menu(object):
    def __init__(self):
        self.title_box_show = 1
        self.title_delimiter = ' > '

    def color_style(self,content,foreground_color,background_color,font_style):
        '''
        输入content，把content设置样式后返回
        :param content:
        :param color:
        :return:
        '''
        foreground = {'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,'dark_green':36,'white':37}
        background = {'black':40,'red':41,'green':42,'yellow':43,'blue':44,'purple':45,'dark_green':46,'white':47}
        style = {'highlight':1,'underline':4}
        foreground_color = foreground.get(foreground_color,'')
        background_color = background.get(background_color,'')
        font_style = style.get(font_style,'')

        return f'\033[{font_style};{foreground_color};{background_color}{content}\033[0m'

    def title_box(self,title):
        if self.title_box_show:
            title_base = "Main Menu" + self.title_delimiter+self.title_delimiter.join(title) if title else "Main Menu"
            print(self.color_style(title_base,'red','blue','highlight'))

    def menu_box(self,steps,title,guide):
        self.title_box(title)

    def draw(self,steps,title=None,guide=None):
        self.menu_box(steps,title,guide)
