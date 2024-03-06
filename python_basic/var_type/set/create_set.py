
'''
create_time: 2024/3/6 15:15
author: yss
version: 1.0
'''

a = {1,2,3}

b = set()
print(a,b)

#集合添加元素
a.add(4)
b.add(5)
print(a,b)
a.update(b)
print(a)


#集合删除元素
a.remove(1)
# b.remove(6)  #元素不存在会抛出 KeyError 异常
a.discard(8)  #discard 删除元素，元素不存在不会报错



