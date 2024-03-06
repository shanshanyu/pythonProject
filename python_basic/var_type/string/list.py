'''
create_time: 2024/3/5 15:04
author: yss
version: 1.0
'''
#把 1~100 内的所有偶数放到一个列表里面去，打印这个列表
#使用列表表达式

a = [x for x in range(2,101) if x%2 == 0]
print(a)