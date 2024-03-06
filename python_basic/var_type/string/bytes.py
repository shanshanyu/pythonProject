'''
create_time: 2023/3/29 21:06
author: yss
version: 1.0
'''
#3 个变量都是字节串
b1 = bytes()

b2 = b''
b3 = b'hello'
print(type(b3))
print(b3.decode())
print(b3)
print(b3[0])
print(b3[1:3])

b4 = bytes('python test',encoding='utf-8') #字节串
print(b4)

b5 = "python string".encode('utf-8') #字节串
print(b5)
print(type(b5.decode()))

b6 = '1234'.encode()  #字符串
print(b6,type(b6))
print(b6[1])

print('hello,你好'.encode('utf-8'))

b7 = b'1'
print(b7)




