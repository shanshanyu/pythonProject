'''
create_time: 2024/4/9 17:13
author: yss
version: 1.0
desc: optoolkit 命令行入口
'''
from tools.menu import Menu


def main():
    m = Menu()
    steps = [
        "test1",
        "test2"
    ]
    pos = m.draw(steps,title=['optoolkit','abc'],guide="【Select】↑ ↓ 【choose】Enter 【Search】s/S 【Quit】q/Q/b/B\
【Page】g/l")
    msg = f"Your choice 【id】：{pos[0]} 【details】：{pos[1]}"
    msg = Menu.color_style(msg,'green','','highlight')
    print(msg)

    if pos[0] == 0:
        pass
    if pos[0] == 1:
        pass




if __name__ == '__main__':
    main()