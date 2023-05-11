'''
create_time: 2023/4/28 10:20
author: yss
version: 1.0
'''

#用 if else 逻辑是否是对的

class Student:
    def __init__(self,name,chinese,math,english):

        self.name = name
        if chinese < 0 or chinese > 100 :
            raise ValueError("number not in [1,100]")
        else :
            self.chinese = chinese
        if math < 0 or chinese > 100 :
            raise ValueError("number not in [1,100]")
        else :
            self.math = math
        if english < 0 or english > 100 :
            raise ValueError
        else :
            self.english = english


    def __repr__(self):
        return "Student<name:{},chinese:{},math:{},english:{}>".format(self.name,self.chinese,self.math,self.english)

tom = Student("tom",1,-88,89)
print(tom)