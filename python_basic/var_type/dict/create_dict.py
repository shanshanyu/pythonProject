'''
create_time: 2024/3/6 17:27
author: yss
version: 1.0
'''
a = {}  #创建字典
b = dict()  #创建字典

c = {x:1 for x in range(3)}
print(a)
print(b)
print(c)

c.pop(2)
print(c)

d = [1,2,3,4]
e = (5,6,7,8)
#使用zip将两个序列压缩成字典

f = dict(zip(d,e))
print(f)