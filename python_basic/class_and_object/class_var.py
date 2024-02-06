'''
create_time: 2023/4/18 14:47
author: yss
version: 1.0
'''

class Parent(object):
    a = 3
    __b = 4
    pass

a = Parent()
Parent.b = 4  #添加类变量
print(a.a)  #用对象的方式访问类变量   3

b = Parent()
print(b.b)  #b是类变量  4
print(b._Parent__b)  #用对象访问类变量  4
