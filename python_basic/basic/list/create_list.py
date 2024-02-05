'''
create_time: 2023/5/27 20:15
author: yss
version: 1.0
'''

#3 种创建列表的方式
'''
1. 通过方括号创建列表
2. 通过内置list函数将字符串，元组，range对象转换成列表
3. 通过列表推导式
'''

a = [1,2,3]
print(a,type(a))


b = list((1,2,3))
b = list({'a':1,'b':2})  #给 list()函数传递字典，会把字典的 key 放在列表中
print(b,type(b))

c = [i for i in range(5)]
print(c,type(c))



d = '[1,2,3]'
d1 = list(d)  #不符合预期，会把 d 当做一个列表元素，字符串
print(d1)

d = [1,2,3]
d = d*3  #列表支持加法和乘法
print(d,type(d))

#list()函数 可以将 元组  字符串   range对象 转换为列表
#tuple()函数可以将列表、range对象转换为元组