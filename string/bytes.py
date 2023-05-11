'''
create_time: 2023/3/29 21:06
author: yss
version: 1.0
'''
#3 个变量都是字节串
b1 = bytes()

b2 = b''
b3 = b'hello'

b4 = bytes('python test',encoding='utf-8') #字节串

b5 = "python string".encode('utf-8') #字节串
print(b5)

print(b4)
print(b3)
print(b3[0])
print(b3[1:3])

print(type(b5.decode()))

