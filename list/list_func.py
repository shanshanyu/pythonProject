'''
create_time: 2023/5/27 20:18
author: yss
version: 1.0
'''

#操作列表的方法
a = [1,2,3,4,5,6]
b = a[1:3]  #列表切片
print(b)

c = {'1':2,'2':3}

#增加列表元素
a.append(4)  #可以添加单个元素，列表，元组，字典，但是这些都会当成单个元素
print(a)

a.extend(b)  #extend向列表中增加一个可迭代对象
print(a)

a.extend(c)  #extend向列表中增加字典，会把字典的 key 加入到列表中
print(a)

a.insert(2,0)  #在位置 2 插入 0
print(a)

#删除列表元素
del a[1]   #删除位置 1 的元素
print(a)

a.remove(4)  #删除列表的某个元素，如果有多个，只删除第一个
print(a)

print(a.pop(3))  #弹出索引位置 3 的元素
print(a)


#清空列表
#a.clear()
#print(a)

#列表中查找元素
print(a.index(3))  #返回元素在列表中的索引
#print(a.index(8))  #如果元素不存在，会抛出一个异常




