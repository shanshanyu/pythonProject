# 2023/11/7 21:02

from abc import ABC,abstractmethod,ABCMeta

class Person(ABC):   #抽象类
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @abstractmethod
    def eat(self):
        pass


class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
    def eat(self):
        print('学生吃蔬菜')


s = Student('zhangsan',15)
s.eat()

