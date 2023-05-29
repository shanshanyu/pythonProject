'''
create_time: 2023/5/29 18:01
author: yss
version: 1.0
'''

import random

print(random.seed())

print(random.randrange(1,4))  #返回 1，4 之间的整数
print(random.randrange(1))  #返回小于 1 的整数，只能是 0

print(random.randint(1000,1500))  #返回 1000<= x <=1500 之间的一个整数，区间是左闭右闭  相当于 randomrange(1000,1500+1)