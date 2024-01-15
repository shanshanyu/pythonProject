'''
create_time: 2023/6/6 10:04
author: yss
version: 1.0
'''

#函数装饰器

def funA(fn):
    print('A')
    fn()
    return 'fkit'  #如果 funA没有返回值，那么 B 就是 None


@funA
def funB():
    print('B')


#print(funB,type(funB))  #funB被替换成了 fkit 字符串
