# 2024/1/25 20:41
'''
列表操作：
列表和列表相加，列表可以乘以一个数字
'''

lst = [1,2,3,4]
lst1 = [2,3,4,5]

lst2 = [9,10,11]
print(lst+lst1)  #列表和列表相加

print(lst*3)  #列表乘以一个数字

print(lst,1 in lst)

print(min(lst2))  #9
print(max(lst2))  #11

print(id(lst2))
lst2.reverse()  #列表反转
print(id(lst2))  #列表反转后还是同一个列表

lst3 = [3,2,5,1]
print(id(lst3))
lst3.sort()
print(id(lst3))  #列表排序后还是同一个列表


lst4 = [3,2,4,6]
print(id(lst4))
print(sorted(lst4))  #使用内置函数 sorted 会返回一个新的列表
print(id(lst4),lst4)