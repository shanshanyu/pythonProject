'''
create_time: 2024/3/7 09:54
author: yss
version: 1.0
'''

a = {1,2,3,4,5,6,7}
b = {5,6,7,8,9,10}

print(a-b)  #计算集合差集
print(a.difference(b))
print(a|b)  #计算集合并集
print(a.union(b))
print(a&b)  #计算集合交集
print(a.intersection(b))
print(a^b)  #计算集合补集
print(a.symmetric_difference(b))
print(a.symmetric_difference_update(b))  #会把运算结果赋值给a集合
print(a)
print(b)