'''
2024/3/25 22:39

re.split 方法


'''

import re

s = 'i,learn,python'

#用 , 分割字符串

res = re.split(r',',s)
print(res)