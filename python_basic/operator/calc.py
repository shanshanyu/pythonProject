'''
create_time: 2023/8/30 15:21
author: yss
version: 1.0
输入两个数，计算两个数在各种运算符下的输出结果
'''

a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a,b,a+b))
print('%d - %d = %d' % (a,b,a-b))
print('%d * %d = %d' % (a,b,a*b))
print('%d / %d = %0.2f' % (a,b,a/b))
print('%d // %d = %d' % (a,b,a//b))
print('%d ** %d = %d' % (a,b,a**b))




