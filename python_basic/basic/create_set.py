'''
create_time: 2023/4/26 10:01
author: yss
version: 1.0
'''
a = {'a'}
print(a)
print(type(a))  #set

a.add('b')

print(a)

a.remove('a')
print(a)

b = set()
print(b)
print(type(b))

a.add(b)