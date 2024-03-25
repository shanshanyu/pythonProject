'''
2024/3/22 17:35
desc: 检查输入的字符串是否是 6 位数字
'''

import re

num = input('input 6 number: ')

res = re.match(r'\d{6}',num)

if res:
    print(res)
else:
    print('未匹配')

