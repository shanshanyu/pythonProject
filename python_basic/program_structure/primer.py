'''
create_time: 2024/3/5 15:14
author: yss
version: 1.0
'''
import sys
import math

#输入一个数，判断这个数是否是素数

for i in range(10,1,-1):
    print(i)


num = int(input('input a number: '))

assert num > 1  #如果这个数小于0断言报错

if num == 2:
    print('{} is primer'.format(num))
    sys.exit(0)


flag = False
for i in range(2,int(num/2-1)):
    if num % i == 0:
        flag = True
        break

if flag:
    print('{} not primer'.format(num))
else:
    print('{} is primer'.format(num))

