'''
create_time: 2024/4/10 09:56
author: yss
version: 1.0

desc: 测试enumerate
'''

a = [1,2,3]
for i in enumerate(a):  #enumerate 对象，用for循环遍历 enumerate 对象的时候，每个元素是一个元组
    print(i,type(i))

