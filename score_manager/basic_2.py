'''
create_time: 2023/4/28 10:33
author: yss
version: 1.0
'''

class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    #用 property 修改 name 方法，相当于为 name 属性添加 getter 方法
    @property
    def name(self):
        return self._name
    #为name属性添加setter方法
    @name.setter
    def name(self,name):
        self._name = name

   # 用 property 修改 name 方法，相当于为 name 属性添加 getter 方法
    @property
    def chinese(self) :
        return self._chinese

    # 为name属性添加setter方法
    @chinese.setter
    def chinese(self, chinese) :
        if chinese < 0 or chinese > 100:
            raise ValueError("number must in [1..100]")
        else:
            self._chinese = chinese

    def __repr__(self):
        return "Student<name:{},chinese:{},math:{},english:{}>".format(self.name,self.chinese,self.math,self.english)

tom = Student("tom",-1,88,89)
print(tom)

print(tom._name)
print(tom.chinese)