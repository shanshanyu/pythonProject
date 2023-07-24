'''
create_time:  22:40
author: yss
version: 1.0
'''

f = open("/usr/local/python_file/test.log","r")

file_data = f.readlines()  #文件对象的 readlines 返回的结果是一个列表
print(file_data,type(file_data))

#移动文件指针
f.seek(0,0)

file_data = f.readline()
print(file_data,type(file_data),file_data.encode())  #readline 读取一行，会读出结尾的换行符 \n




for i in f.readlines():   #f.readlines()返回所有行组成的列表
    i = i.strip()
    print(i)
print(type(f.readlines()))
f.close()
print(f.encoding)
print(f.closed)
