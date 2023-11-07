# 2023/11/7 21:14

#type是类，而且是元类，用来创建类的类叫做元类  type 是元类

class Student:
    pass

print(type(Student))   #Student 类的类型是 type，说明 Student 类是 type 类的实例

#使用type来创建一个类

def fun(self):
    print('fun')


Dog = type('Dog',(object,),dict(walk=fun,age=6))  #dict是类变量和类方法

d = Dog()

print(type(d))
d.walk()
print(Dog.age)