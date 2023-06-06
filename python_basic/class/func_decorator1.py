'''
create_time: 2023/6/6 10:04
author: yss
version: 1.0
'''

#函数装饰器

def funA(fn):
    print('A')
    fn()
    return 'fkit'

@funA
def funB():
    print('B')

print(funB,type(funB))  #funB被替换成了 fkit 字符串