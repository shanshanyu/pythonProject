'''
create_time: 2023/4/28 09:31
author: yss
version: 1.0
'''
import sys

class Student:
    def __init__(self,name,chinese,math,english):
        try:
            self.name = name
            if chinese < 0 or chinese > 100:
                raise
            else:
                self.chinese = chinese
            if math < 0 or chinese > 100:
                raise
            else:
                self.math = math
            if english < 0 or english > 100:
                raise
            else:
                self.english = english
        except Exception as e:
            print("error: ",e)
            sys.exit(1)

    def __repr__(self):
        return "Student<name:{},chinese:{},math:{},english:{}>".format(self.name,self.chinese,self.math,self.english)

tom = Student("tom",1,-88,89)
print(tom)
