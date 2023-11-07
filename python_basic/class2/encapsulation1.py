'''
create_time: 2023/11/7 10:42
author: yss
version: 1.0
'''

class Test(object):
    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)


if __name__ == '__main__':
    test = Test('11')
    print(test._Test__foo)  # 访问实例变量   实例变量的封装
    test._Test__bar()  # 访问实例方法