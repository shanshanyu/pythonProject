'''
create_time: 2023/5/28 08:15
author: yss
version: 1.0
'''


a = ['1','2','3']
with open('test.txt','w',encoding='utf-8') as file:
    file.writelines('abcd')   #writelines 的参数是一个列表  readlines 的返回值是一个列表
    #参数是一个字符串也可以,参数需要是一个可迭代对象