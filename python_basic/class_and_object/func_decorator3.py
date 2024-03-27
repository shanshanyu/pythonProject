'''
create_time: 2023/11/7 11:35
author: yss
version: 1.0
函数装饰器
'''

class Student(object):
    def __init__(self,name):
        self.__name = name

    @property   #函数装饰器，装饰 name   把 name1 方法设置成 name1 属性的 get 方法
    def name1(self):
        print('get 方法执行了')
        return self.__name

    @name1.setter
    def name1(self,name):   #把 name1 方法设置成 name1 属性的 set 方法
        print('set方法执行了')
        self.__name = name

if __name__ == '__main__':
    s = Student('zhagnsan')
    s.name1 = 'lisi'
    print(s.name1)

