'''
create_time: 2024/1/4 22:53
author: yss
version: 1.0
测试 filter 函数（内置函数）
'''

lst = [1,2,3,4]
def is_old(x):
    return x % 2 == 0

res = filter(is_old,lst)
print(res,type(res))
