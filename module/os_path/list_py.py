# 2023/5/24 22:30
#列出指定目录下所有的 python 文件

import os
import os.path



def list_py(path):
    if not os.path.isdir(path):
        print('input is not a path')
        return
    for i in os.listdir(path):
        #print(os.path.splitext(i))
        #print(i)
        #if os.path.splitext(i)[1] == '.py':  #用字符串中的 endwith 来实现更好
        #    print(i)
        if os.path.isfile(i) and i.endswith('.py'):
            print(i)

if __name__ == '__main__':
    path = input('input path to search py: ')
    list_py(path)


'''
os.path模块的方法：
abspath  获取绝对路径
dirname   获取上层目录
basename   

join  拼接目录
exists  文件或目录是否存在


walk

'''

