'''
create_time: 2024/4/7 16:10
author: yss
version: 1.0

在一堆字符串中找出匹配的电话号码

通过 (?<=..) 和 (?=...)实现

电话号码分为 1[34578]xxx
'''

import re
import time


def main():
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')

    # findall 把所有匹配字符串放入一个列表中
    res = pattern.findall(sentence)
    print(res)

    # finditer 把所有的匹配结果放在一个迭代器中
    iterator = pattern.finditer(sentence)
    for i in iterator:
        print(i)

    # 提取所有的匹配字符串
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())
        time.sleep(1)



if __name__ == '__main__':
    main()