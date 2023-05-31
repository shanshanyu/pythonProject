'''
create_time: 2023/5/30 19:36
author: yss
version: 1.0
'''

#列表嵌套字典的迭代   json 数据解析的时候会用到

#列表嵌套列表   元组嵌套元组

a = (1,4,3)
#a.sort()   #元组没有sort方法
b = list(a)
b.sort(reverse=True) #sort()方法并不返回值
print(b)

c = set()
c.add(1)
c.add(2)
c.add(3)
c.add(4)
c.add('4')

for i in c:
    print(i)