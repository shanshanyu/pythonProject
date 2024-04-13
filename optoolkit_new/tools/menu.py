# 2024/4/13  20:56


class Menu(object):
    def __init__(self):
        self.title_box_show = 1
        self.title_delimiter = ' > '

    def title_box(self,title):
        if self.title_box_show:
            title_base = "Main Menu" + self.title_delimiter.join(title) if title else "Main Menu"

    def menu_box(self,steps,title,guide):
        self.title_box(title)

    def draw(self,steps,title=None,guide=None):
        self.menu_box()
