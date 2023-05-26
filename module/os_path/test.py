'''
create_time: 2023/5/10 16:11
author: yss
version: 1.0
'''

import os.path
import sys

sys.argv.append('conf_file')
print(os.path.exists('/Users'))
print(os.path.exists('/tmp1'))   #判断文件或目录是否存在

print(os.path.abspath('.'))  #获取文件或目录的绝对路径


abs_path = os.path.abspath('.')
print(abs_path)
print(os.path.dirname(abs_path))  #获取文件或目录的上层目录名

print(os.path.exists('./path.py'))
print(os.path.abspath('path.py'))  #获取文件或目录的绝对路径
file_abs_path = os.path.abspath('path.py')
print(file_abs_path)

print(os.path.exists(file_abs_path))  #判断文件或目录是否存在
print(os.path.dirname(file_abs_path))  #获取文件所在目录
print(os.path.isfile(file_abs_path))  #判断是否是文件

print(os.path.getsize(file_abs_path))  #查看文件大小

print(os.path.exists('path.py'))

join_path = os.path.join(os.path.abspath('.'),'path.py')  #拼接文件或目录
print(join_path)


abs_path = os.path.abspath(__file__)
print(os.path.basename(abs_path))

#splitext  分离文件名和扩展名

#split  拆分 dirname 和 basename

print(os.path.isdir('D:\pythonProject\module'))