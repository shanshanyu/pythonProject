'''
create_time: 2023/5/29 10:26
author: yss
version: 1.0
'''
#__new__ 方法和 __init__ 方法   new 方法创建对象，init 方法初始化对象，
print(dir(object))  #查看 object类中有哪些属性和方法

class Person(object):
    def __init__(self,name,age):
        print('__init__被调用了,初始化的对象id 为{}'.format(id(self)))
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):  #__new__方法是 object 类中的静态方法!!!
        print('__new__ 被调用了,cls的id为{}'.format(id(cls)))
        obj = super().__new__(cls)  #调用 object 类中的 __new__ 方法,创建一个 Person 对象
        print('创建对象的 id 为 {}'.format(id(obj)))
        return obj   #__new__ 需要返回创建的 id

p = Person('zhangsan',15)
