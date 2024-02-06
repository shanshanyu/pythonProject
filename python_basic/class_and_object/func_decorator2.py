'''
create_time: 2023/6/6 10:11
author: yss
version: 1.0
'''
#函数装饰器

#创建一个只读属性，然后通过函数装饰器来操作
#class property(get,set,del,docstr)
class Student(object):
    def __init__(self,name):
        self.__name = name


    def name1(self):
        return self.__name


    def name2(self,name):
        self.__name = name


    def test1(self):
        del self.__name

    #这种方式也可以
    name = property(name1,name2,test1,'func decorator')







if __name__ == '__main__':
    p = Student('zhangsan')
    print(p.name)
    p.name = 4
    print(p.name)
    #del p.name
    #print(p.name)