'''
create_time: 2024/3/18 15:41
author: yss
version: 1.0

desc：一个 Pet 类的抽象基类，两个子类，猫、狗
抽象类
抽象方法
'''

from abc import ABCMeta,abstractmethod


class Pet(object,metaclass=ABCMeta):  #也可以直接继承 ABC
    @abstractmethod
    def make_voice(self):
        '''
        发出声音
        :return:
        '''
        pass


class Dog(Pet):
    def make_voice(self):
        print('dog 的叫声是 汪汪')


class Cat(Pet):
    def make_voice(self):
        print('cat 的叫声是 喵喵')


def main():
    d = Dog()
    d.make_voice()
    c = Cat()
    c.make_voice()


if __name__ == '__main__':
    main()


