'''
create_time: 2024/4/2 14:22
author: yss
version: 1.0

测试 defaultdict 类，创建对象后，如果直接写成 a[x] 不赋值会怎样
创建 defaultdict对象，为 访问 defaultdict 对象的某个 key，然后打印 defaultdict对象
'''

from collections import defaultdict

d = defaultdict(list)
lst = ['abc','cde']
for i in lst:
    d[i]

print(d)



