'''
create_time: 2023/5/29 21:10
author: yss
version: 1.0
'''

#计算水仙花数
import math

for i in range(100,1000):
    n3 = i//100         #取百位   十位   个位   math.pow
    #n2 = (i-100)//10
    n2 = i // 10 % 10
    n1 = i % 10
    if n3**3 + n2**3 + n1 **3 == i:
        print(i)

print('-'*100)

for i in range(100,1000):
    if math.pow(i//100,3) + math.pow(i//10%10,3) + math.pow(i%10,3) == i:  #把一个数拆分，如果要取左边的数就整除，如果要取右边的数就取余
        print(i)
