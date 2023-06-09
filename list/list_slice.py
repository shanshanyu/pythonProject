'''
create_time: 2023/5/31 15:37
author: yss
version: 1.0
'''

a = [1,2,3,4,5]

#将 3 4 替换成 'a' 'b'
a[2:4] = ['a','b']
print(a)  #替换成功  [1, 2, 'a', 'b', 5]

print('-' * 100)

a = [1,2,3,4,5]
#将 3 4 替换成 'a'  'b' 'c'
a[2:4] = ['a','b','c']
print(a)  #替换成功 [1, 2, 'a', 'b', 'c', 5]   不要求数量相等

print('-' * 100)

a = [1,2,3,4,5]
a[2:4]  = []  #删除下标为 2  3 的 元素
print(a)

print('-' * 100)

a = [1,2,3,4,5]
a[2:5:2] = ['a','b']  #如果带了 step，列表的元素数量要求一致
a.append(1)
print(a)
#a.remove(1)  #删除列表元素，如果有多个只删除一个
a.pop(1)
print(a)

a = [1,2,3,4,5]
a[:] = [2]  #列表切片当左值会覆盖修改源列表
print(a)

a = [1,2,3,4,5]
print(id(a),id(a[:]))  #列表整个切片和原列表是不相等的

b = ['a','b','c']
a = a+b  #会得到一个新的列表对象
print(id(a))

a = [1,2,3,4,5]
b = a[:]
print('id(a) = {}'.format(id(a)))
print('id(b) = {}'.format(id(b)))  #b 是 a 的浅拷贝，a和b的值不相等

print(id(a[0]),id(b[0]))  #a[0] 和 b[0] 的值是相等的


