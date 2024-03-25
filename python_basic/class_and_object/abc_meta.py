'''
create_time: 2024/3/14 21:50
author: yss
version: 1.0

metaclass：元类

metaclass应该继承type类，并重写 __new__() 方法

ABC 是一个抽象基类
ABCMeta 是元类
'''

import abc

from abc import ABCMeta
from abc import ABC
