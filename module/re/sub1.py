'''
create_time: 2024/4/7 16:40
author: yss
version: 1.0

替换字符串中的不良内容
'''
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    pattern = re.compile(r'傻叉|fuck|操',flags=re.IGNORECASE)
    res = pattern.sub('*',sentence)

    # res = re.sub(r'傻叉|fuck|操','*',sentence,flags=re.IGNORECASE)
    print(res)


if __name__ == '__main__':
    main()
