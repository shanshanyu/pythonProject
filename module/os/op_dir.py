# 2023/5/24 22:22

import  os
import os.path
#print(os.getcwd())   #获取当前工作路径

for root,dirs,files in os.walk(os.getcwd()):

    print(root,dirs,files)


#print(os.listdir('../'))

#os.mkdir('test_dir')  #创建一个目录

#os.makedirs('test1/test2')  #创建多级目录

#os.rmdir('test_dir')   #删除一个目录
#os.removedirs('test1/test2')  #删除多级目录

#os.system('notepad')  #执行命令，打开记事本
#cur_dir = os.path.abspath('.')
#print(cur_dir)
#os.startfile(os.path.join(cur_dir,'create_workbook.py'),'print')

'''
os模块的常用方法
操作目录：
listdir  列出目录下的内容
mkdir
mkdirs
rmdir
rmdirs


system  执行命令
startfile  执行文件

getcwd  获取工作目录
chdir   改变工作目录

'''

