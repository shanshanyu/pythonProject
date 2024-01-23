# 2024/1/11 22:56
'''
 python3构造方法：
 默认会有一个空参构造 def __init__(self),继承自object

子类会继承父类的构造方法和其他的方法
'''


class Person(object):
    def __init__(self):
        print('person 构造方法执行了')

    def play(self):
        print('parent play')


class Student(Person):
    def __init__(self, name='zhangsan'):
        super().__init__()
        self.name = name

if __name__ == '__main__':
    s = Student()
    s.play()


