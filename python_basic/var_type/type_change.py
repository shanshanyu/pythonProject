'''
create_time: 2023/3/29 22:11
author: yss
version: 1.0
'''

#强制类型转换  int float 转 str，str 转int，str 转float

a = 3.14
c = '123'
d = '123.4'  #字符串里面需要是整数，不能是小数
b = "abc"  #字符串转不了

print(int(a),type(int(a)))

print(int(c),type(int(c)))
#print(int(d),type(int(d)))
#print(int(b),type(int(b)))
print(int(True))

print(float(d),type(float(d)))
print(float(c),type(float(c)))

print(str(a),type(str(a)))