'''
create_time: 2023/4/18 11:59
author: yss
version: 1.0
'''
class Parent1(object):
    def __init__(self, arg1):
        self.arg1 = arg1
        print("parent1 init run")

class Parent2(object):
    def __init__(self, arg2, arg3):
        self.arg2 = arg2
        self.arg3 = arg3
        print("parent2 init run")

class Child(Parent1, Parent2):
    '''
       使用super()函数调用父类的构造方法。多继承中，该函数只能调用第一个直接父类的构造方法。在 python3 中 super 函数不需要传参
    '''
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1)
        #super(Parent2,self).__init__(arg2, arg3)
        Parent2.__init__(self,arg2,arg3)
        #super(Child, self).__init__(arg2, arg3)
        #self.arg4 = arg4


a = Child(1,2,3)