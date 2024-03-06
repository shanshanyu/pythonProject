'''
create_time: 2024/3/5 17:39
author: yss
version: 1.0
'''
#变量的作用域  局部变量  全局变量

def foo():
    a = 200  #局部变量a
    print(a)
    print(locals())

if __name__ == '__main__':
    a = 100  #全局变量a
    foo()
    print(a)
    print(globals())

