'''
create_time: 2023/12/29 17:26
author: yss
version: 1.0
'''


def color_style(string, mode="", font_color="", background="") :
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
    #模式，字体，背景色
    _style = ";".join([s for s in [mode, fore, back] if s])
    style = f"\033[{_style}m"
    end = f"\033[{_end}m"
    return f"{style}{string}{end}"


if __name__ == '__main__':
    res = color_style('hello')
    print(res)