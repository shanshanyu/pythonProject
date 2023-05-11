'''
create_time: 2023/5/11 11:12
author: yss
version: 1.0
'''
import os
print(os.name)  #posix

print(os.environ)
print(type(os.environ))  #环境变量的类型

print(os.getcwd())   #获取当前的工作目录

print(os.getlogin())