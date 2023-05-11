'''
create_time:  22:40
author: yss
version: 1.0
'''

f = open("/usr/local/python_file/test.log","r")
for i in f.readlines():   #f.readlines()返回所有行组成的列表
    i = i.strip()
    print(i)
print(type(f.readlines()))
f.close()
print(f.encoding)
print(f.closed)