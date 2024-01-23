'''
create_time: 2023/5/27 22:11
author: yss
version: 1.0
'''

a = eval('7')   #eval 用来执行字符串表达式
print(a)

b = eval('2+3')
print(b)


d = '{1:2,3:4}\n'
print(eval(d),type(eval(d)))  #可以把字符串包含的字典转换成字典