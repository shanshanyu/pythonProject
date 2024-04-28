'''
create_time: 2023/3/29 22:39
author: yss
version: 1.0
'''
print(3+4)
print(2**3)
print(9//4)
print(-9//4)
print(9%4)
print(9%-4)
print(-9%4)

a = 3
b = 4
print("a = ",a)
print("b = ",b)

a,b = b,a
print("a = ",a)
print("b = ",b)

#序列封包和序列解包
a,*b,c = range(10)
print(a)
print(b)
print(c)

#位运算符   交换2个数，不适用中间变量
a = 3
b = 4
a = a^b
b = a^b
a = a^b
print(a)
print(b)

#进制转换
a = 10   #10进制转换成其他进制
print(bin(a))
print(oct(a))
print(hex(a))

#其他进制转换成10进制
b = bin(a)
print(b)
print(type(b))
c = int(b,2)
print(c)


print(bool(''))


#条件表达式
a = 3
b = 4
c = b if b < a else a
print(c)