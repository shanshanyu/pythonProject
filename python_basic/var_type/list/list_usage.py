'''
create_time: 2024/3/6 14:25
author: yss
version: 1.0
'''

a = [1,2,3,4,5,3,4,5]
c = [6,7,8]
#添加元素
a.append(6) #加到最后
a.insert(-1,7)
print(a)
print(a.count(3))  #统计元素的个数
print(a.index(6))  #如果找不到会抛出异常
a.extend(c)
print(a)

#移除元素
a.remove(8)  #remove删除元素得保证元素存在
a.pop(-1)  #按照下标移除元素
print(a)

#查找元素
print(a.index(5)) #index方法，元素不存在会报错

#排序和翻转
a.reverse()  #reverse 是永久排序
print(a)
a.sort()  #sort是永久排序
#sorted 方法是临时排序
print(a)



b = '1234567'
print(b.index('7'))  #字符串的 index 方法，如果元素不存在会报错
print(b.find('8'))  #字符串的 find 方法

