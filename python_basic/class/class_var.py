'''
create_time: 2023/4/18 14:47
author: yss
version: 1.0
'''

class Parent(object):
    a = 3
    _b = 4
    pass

a = Parent()
Parent.b = 4
print(a.a)

b = Parent()
print(b.b)
print(b._b)
