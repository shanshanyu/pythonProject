'''
create_time: 2023/4/18 17:01
author: yss
version: 1.0
'''
class Parent1:
    def __init__(self,arg1):
        self.arg1 = arg1
    def p1(self):
        print("parent1")

class Parent2:
    def __init__(self,arg2,arg3):
        self.arg2 = arg2
        self.arg3 = arg3
    def p2(self):
        print("parent2")
        print(self.arg2)

class Child(Parent1,Parent2):
    def __init__(self,arg1,arg2,arg3):  #子类重写父类的构造方法
        #super().__init__(arg1)   #super才能重写第一个直接父类的构造方法
        Parent1.__init__(self,arg1)
        Parent2.__init__(self,arg2,arg3)

a = Child(1,2,3)
a.p1()
a.p2()