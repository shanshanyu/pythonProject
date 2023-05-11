'''
create_time:  21:21
author: yss
version: 1.0
'''

print("hello\nworld")
print("hello\tworld")
print("http://www.baidu.com")
a = b'abcd'
print(type(a))
b = a.decode()
print(b)

with open("/tmp/out","a+",True) as f:
    print("hello jerrry", file=f)
    print(f.read())

f.close()
