'''
create_time: 2024/3/7 10:46
author: yss
desc: 实现跑马灯效果
version: 1.0
显示一段文字，abc  bca  cba ...

清屏->打印abc->停止0.5s->清屏->修改内容为bca->打印bca

'''

import time
import os


def main():
    content = '北京欢迎你为你开天辟地。。。'
    os.system('clear')
    while True :
        print(content)
        time.sleep(0.5)
        os.system('clear')
        content = content[1 :] + content[0]


if __name__ == '__main__':
    main()



