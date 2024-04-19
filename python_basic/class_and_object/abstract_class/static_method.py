'''
create_time: 2024/4/18 18:56
author: yss
version: 1.0

静态方法能在类中直接被调用吗
'''


class Student(object):
    def __init__(self):
        self.name = 'zhangsan'

    @staticmethod
    def play():
        print('i play')

    def say(self):
        Student.play()  # 静态方法调用建议用类名调用


if __name__ == '__main__':
    s = Student()
    s.say()