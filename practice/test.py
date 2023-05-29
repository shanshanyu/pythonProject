'''
create_time: 2023/5/29 17:43
author: yss
version: 1.0
'''

print('abc'.isidentifier())  #是一个合法的标识符
print('abc'.isalpha()) #True
print('abc4'.isalpha()) #False
print('123'.isdigit()) #True

print('123'.isnumeric()) #True
print('123'.isdecimal()) #True

print(' \n'.isspace())  #只包含空白字符返回True

print('0xa010'.isdigit())  #False