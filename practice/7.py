'''
create_time: 2023/5/30 11:23
author: yss
version: 1.0
'''

#zip 压缩两个列表后，可以直接用 dict 转换成字典  dict(zip(lst1,lst2))

lst1 = [1,2,3]
lst2 = ['a','b','c']

d = dict(zip(lst1,lst2))
print(d)

if 5 in d.keys():
    print(1,d[1])
else:
    print('not exist')


a = ([1,2],[3,4])  #元组不可以修改，元组中包含可变元素的话，可变元素可以修改

print(a)
a[0][1] = 3
print(a)

