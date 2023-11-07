'''
create_time: 2023/11/7 10:38
author: yss
version: 1.0
python的封装，这种方式访问带 __ 的属性或方法是有问题的
'''

class Test(object):
    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)


if __name__ == '__main__':
    test = Test('11')
    print(test.__foo)   #访问实例变量   实例变量的封装
    test.__bar()    #访问实例方法
