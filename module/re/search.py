'''
2024/3/25 22:19

在一串字符串中找到匹配的字符串
'''

import re

prog = re.compile(r'\d\.\d+')

string = 'i learn python 3.9,and 3.7'

res = prog.search(string)
if res:
    print('匹配起始位置',res.start())
    print('匹配结束位置',res.end())
    print('匹配区间',res.span())
    print('原始字符串: ',res.string)
    print('匹配的字符串: ',res.group())
    print('匹配的字符串1: ',res.groups())
    print(type(res.group()))

    print(re.findall(r'(\d)\.\d+',string))  #findall的用法，和捕获组有关系
    '''
    如果没有组，返回与整个模式匹配的字符串列表。如果有且仅有一个组，
    返回与该组匹配的字符串列表。如果有多个组，返回与这些组匹配的字符串元组列表。非捕获组不影响结果。
    '''


