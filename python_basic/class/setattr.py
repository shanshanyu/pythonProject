'''
create_time: 2023/4/27 10:01
author: yss
version: 1.0
'''
class Student:
    def __setattr__(self,key,value):
        #self.key = value  #这种方式会导致死循环
        self.__dict__[key] = value

a = Student()
a.b = 1
print(a.b)
