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
print(os.system('dir'))  #执行命令

parent_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(parent_path,'time\cur_time.py')
print(file_path)
os.startfile(file_path)