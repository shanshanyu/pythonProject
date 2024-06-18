'''
create_time: 2023/6/6 09:40
author: yss
version: 1.0
'''

#函数装饰器

#创建一个只读属性，然后通过函数装饰器来操作
#class property(get,set,del,docstr)
class Student(object):
    def __init__(self,name):
        self.__name = name

    @property   #函数装饰器，装饰 name
    def name(self):
        print('get 方法执行了')
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


if __name__ == '__main__':
    p = Student('zhangsan')
    print(p.name)
    p.name = 4
    print(p.name)
    del p.name
    print(p.name)