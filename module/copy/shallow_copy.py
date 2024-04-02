'''
create_time: 2024/4/2 11:56
author: yss
version: 1.0
浅copy

Python 的赋值语句不复制对象，而是创建目标和对象的绑定关系。对于自身可变，或包含可变项的集合，有时要生成副本用于改变操作，而不必改变原始对象。
'''
import copy

a = [1,2,[3,4]]

b = a  #直接赋值,等于加了个引用指向列表对象

c = copy.copy(a)

print(a,c)

a.append(6)
print(a,c) #说明[1, 2, [3, 4], 6] [1, 2, [3, 4]]  父对象是复制了，子对象没有复制

a[2].append(7)
print(a,c)  #说明子对象没有复制

d = copy.deepcopy(a)
print(a,d)

a[2].append(8)
print(a,d)  #[1, 2, [3, 4, 7, 8], 6] [1, 2, [3, 4, 7], 6]  说明深copy把父对象和子对象都复制了