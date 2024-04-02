'''
create_time: 2024/4/2 15:48
author: yss
version: 1.0

字典排序
'''

a = {1:[1,2,5,6],2:[3,4,5]}
print(a.items())
print(sorted(a.items(),key=lambda x:len(x[1])))  #根据字典 value 的长度进行排序
