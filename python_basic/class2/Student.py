'''
create_time: 2023/11/1 10:43
author: yss
version: 1.0
'''

class Student(object):
    name = 'lisi'   #类变量
    age = 15

    b = 3

    @classmethod    #类方法
    def play(cls):
        print("class method")


    @staticmethod   #静态方法
    def eat():
        print("静态方法eat")

    def __init__(self,name,age):   #如果定义了带参的构造方法，默认的无参构造就不存在了
        self.name = name   #实例变量
        self.age = age

    def show(self):   #实例方法
        print(self.name,self.age)


if __name__ == '__main__':
    s = Student('zhangsan',15)
    s.show()  #通过对象调用实例方法

    print(s.name)  #通过对象调用实例属性
    print(Student.name)   #通过类访问类变量

    Student.play()   #通过类访问静态方法

    Student.eat()

    s.eat()