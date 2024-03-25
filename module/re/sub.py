'''
2024/3/25 22:33

re.sub 用来做一些替换，可以屏蔽一些字符

比如先屏蔽 密码
'''

import re

s = '给我看看你的密码'

res = re.sub(r'密码','**',s)
print(res)