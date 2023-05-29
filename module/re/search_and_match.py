'''
create_time: 2023/5/29 17:27
author: yss
version: 1.0
'''

import re

prog = re.compile('\d{6}')
res = prog.search('123456') #search 会有一个  start  end 参数，match 没有，search 比 match 更精细
print(res)