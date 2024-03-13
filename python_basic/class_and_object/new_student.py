'''
create_time: 2024/3/8 10:52
author: yss
version: 1.0
'''

class Student(object):
    '''
    一个学生类对象
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,book):
        print(f'{self.name} 正在学习{book}')

if __name__ == '__main__':
    s = Student('zhangsan',15)
    s.study('数学')
    print(Student.__doc__)
