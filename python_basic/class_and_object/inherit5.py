'''
create_time: 2024/3/8 16:10
author: yss
version: 1.0

属性要封装，用 _ 开头，不要用 _ 表示
继承：
父类 person，有name 和 age 属性

子类 teacher，有 title 属性

子类 student，有 grade 属性
'''


class Person(object):
    '''
    人
    '''
    def __init__(self,name,age):
        self._name = name
        self._age = age

    #如果没有对属性做一些判断，没有必要用 @property 装饰器
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age <= 0:
            print('年龄输入有误')
        else:
            self._age = age

    def eat(self):
        print(f'{self.name} 在吃饭')

class Teach(Person):
    '''
    老师
    '''
    def __init__(self,name,age,title):
        Person.__init__(self,name,age)  #使用非绑定方法，需要传递 self
        self._title = title

    #property装饰器把 get set 方法变成了属性，用方法的好处是可以做一些判断
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        self._title = title

    def teach(self,book):
        print(f'{self.title} 的老师{self.name} 正在教学 {book}')

class Student(Person):
    '''
    学生
    '''
    def __init__(self,name,age,grade):
        Person.__init__(self,name,age)
        self._grade = grade

    @property
    def grade(self):
        return self.grade
    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.age} 的 {self.name} 正在看熊出没')
        else:
            print(f'{self.age} 的 {self.name} 正在看小电影')


def main():
    t = Teach('lisi',38,'high')
    t.teach('math')


if __name__ == '__main__':
    main()