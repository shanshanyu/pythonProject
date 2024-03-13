'''
create_time: 2024/1/11 10:58
author: yss
version: 1.0
'''

class Person:
    def __init__(self):
        print('person 的构造方法被调用了')


class Student(Person):
    def __init__(self):
        super().__init__()
        print('student 的构造方法被调用了')


if __name__ == '__main__':
    '''
    Q:测试一下在创建子类对象时会不会调用父类的构造方法？
    A:不会，需要手动调用
    '''
    s = Student()
