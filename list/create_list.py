'''
create_time: 2023/5/27 20:15
author: yss
version: 1.0
'''

#3 种创建列表的方式

a = [1,2,3]
print(a,type(a))


b = list((1,2,3))
b = list({'a':1,'b':2})  #给 list()函数传递字典，会把列表的 key 放在列表中
print(b,type(b))

c = [i for i in range(5)]
print(c,type(c))



d = '[1,2,3]'
d1 = list(d)  #不符合预期，会把 d 当做一个列表元素，字符串
print(d1)