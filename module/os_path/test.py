'''
create_time: 2023/5/10 16:11
author: yss
version: 1.0
'''

import os.path
import sys

sys.argv.append('conf_file')
print(os.path.exists('/Users'))
print(os.path.exists('/tmp1'))

print(os.path.abspath('.'))


abs_path = os.path.abspath('.')
print(abs_path)
print(os.path.dirname(abs_path))

print(os.path.exists('./path.py'))
print(os.path.abspath('path.py'))  #获取文件或目录的绝对路径
file_abs_path = os.path.abspath('path.py')
print(file_abs_path)

print(os.path.exists(file_abs_path))  #判断文件或目录是否存在
print(os.path.dirname(file_abs_path))  #获取文件所在目录
print(os.path.isfile(file_abs_path))  #判断是否是文件

print(os.path.getsize(file_abs_path))  #查看文件大小

print(os.path.exists('path.py'))

join_path = os.path.join(os.path.abspath('.'),'path.py')
print(join_path)

