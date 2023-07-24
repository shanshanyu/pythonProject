# 2023/5/24 21:37
# with语句管理的资源是一个上下文管理器，需要实现 __enter__ 和 __exit__ 方法
class ContextMgr(object):
    def __enter__(self):
        print('enter')
        return self  #enter 需要返回值，把返回值赋值给 as 后的变量
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit exec')

    def test(self):
        print('1')


with ContextMgr() as f:
    #print('hello')
    f.test()

#a = ContextMgr()
#a.show()
