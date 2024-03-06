'''
create_time: 2024/3/5 17:51
author: yss
version: 1.0
'''

count = 1 #全局变量 count
def a():
    count = 2 #局部变量count
    def b():
        nonlocal count  #指的是嵌套作用域 a 中的 count 变量
        print(count)
        count = 3  #把 2 改成了 3
    b()
    print(count)


if __name__ == '__main__':
    a()
    print(count)  #访问全局变量count
