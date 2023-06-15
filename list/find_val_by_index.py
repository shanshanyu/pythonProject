'''
create_time: 2023/6/14 09:36
author: yss
version: 1.0
'''
a = [1,2,3,4]

b = ['a','b','c','d']

#a b 长度一样，根据 a b 创建一个字典

d = dict(zip(a,b))
print(d)

#创建多个字典，每个字典一对  1:'a'   2:'b' ..


print(d)
a = [1,2,3,4]
b = ['a','b','c','d']
for ip in a:
    d[ip] = {ip:b[a.index(ip)]}  #这种方式每次循环都需要执行 index 函数，线性检索一次，效率低

print(d)


for index,ip in enumerate(a):  #这种方式效率更高
    d[ip] = {ip:b[index]}

print(d)