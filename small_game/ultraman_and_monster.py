'''
create_time: 2023/11/7 16:50
author: yss
version: 1.0
'''

from abc import ABCMeta,abstractmethod


class Fighter(metaclass=ABCMeta):
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        self._name = name
        self._hp = hp

    @property  #用property修饰方法，把方法变成属性
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp

    @property
    def alive(self):
        '''
        判断是否存活
        :return:
        '''
        return self._hp > 0

    @abstractmethod
    def attack(self):
        ''''
        攻击
        '''
        pass

if __name__ == '__main__':
    f = Fighter('zhagnsan',100)



