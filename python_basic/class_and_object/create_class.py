'''
create_time: 2023/4/18 14:55
author: yss
version: 1.0
'''

class Parent(object):
    hair = 'black'  #类变量
    def __init__(self,name,age):
        self.name = name  #实例变量
        self.age = age
    def say(self,content):
        print(content)
    def run(self):
        self.say("hahaha")
        print("wawawa")

    @classmethod
    def show(cls):
        print('这是类方法')

a = Parent('yss',32)
a.say("真男人")
#del a.say
a.say("hahaha")

a.run()

b = a.run  #将实例方法赋值给变量，可以做到自动绑定对象
b()

print(dir(Parent))
print(dir(a))
Parent.show()  #调用类方法