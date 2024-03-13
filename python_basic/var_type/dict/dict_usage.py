'''
create_time: 2024/3/6 17:43
author: yss
version: 1.0
'''
a = {1:2,3:4,5:6}
print(a)

#访问字典元素值
print(a[1])
# print(a[2])  #key不存在会报错 KeyError
print(a.get(2))  #key不存在不会报错


#添加字典元素
a['a'] = 3
print(a)
a.update({4:'b'})
print(a)


#删除字典元素
a.pop(1)
print(a)
del a[3]
print(a)

print(a)
print(a.setdefault(5,'c'))
print(a)

print(a.pop(5,3))
print(a)
a.clear()
print(a)
