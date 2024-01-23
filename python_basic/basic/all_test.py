'''
create_time: 2023/7/5 13:08
author: yss
version: 1.0
'''

a = all(i for i in range(1,5))  # True

b = (i for i in range(3))
print(type(b))

c = [i for i in range(3)]
print(type(c))   #列表

d = {3:0 for i in range(3)}
print(type(d))  #字典
print(a)
