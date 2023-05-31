'''
create_time: 2023/5/30 20:52
author: yss
version: 1.0
'''

#求圆的周长和面积
'''
import math
a = int(input('输入半径：'))
b = math.pi * math.pow(a,2)
print(b)
print('{:.2f}'.format(b))

'''


#如果有些变量频繁被一些函数使用到，可以考虑定义成一个类，变量定义成实例变量

import math

#定义一个圆类
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        print('%.2f' % (2*math.pi*self.radius))  #格式化字符串

    def area(self):
        print('%.2f' % (math.pi * math.pow(self.radius,2)))


if __name__ == '__main__':
    try:
        radius = int(input('请输入半径：'))
        c = Circle(radius)
        c.perimeter()
        c.area()
    except Exception as e:
        print(e)