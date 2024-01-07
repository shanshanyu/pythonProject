'''
create_time: 2024/1/5 16:34
author: yss
version: 1.0
'''

#异常处理的完整结构如下，try 里面是可能异常的代码，except 捕获到异常后执行，else是没有捕获到异常执行，finally是都会执行的。

#如果 try 里面有 return，还是会执行 finally.

#如果 try 里面有 return，异常了会执行 except+finally，不会执行else
#如果 try 里面有 return， 没有异常直接返回了，也不会执行 else


def divede(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('除 0 异常')
    else:
        print('计算成功!')
    finally:
        print('计算完了!')


if __name__ == '__main__':
    divede(3,1)