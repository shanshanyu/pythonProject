'''
create_time: 2023/4/18 10:25
author: yss
version: 1.0
'''

#方法覆盖
class BaseClass:
    def foo(self):
        print("父类foo方法")

class SubClass(BaseClass):
    def foo(self):
        print("子类foo方法")
    def bar(self):
        print("执行foo方法")
        self.foo()  #重写父类的foo方法
        BaseClass.foo(self)

a = SubClass()
a.bar()