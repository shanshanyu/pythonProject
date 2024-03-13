'''
create_time: 2023/11/7 11:51
author: yss
version: 1.0
判断三条边能否构成三角形
'''

class Triangle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod  #判断是否能构成圆不是圆的方法，用静态方法
    def is_valid(a,b,c):
        return a+b > c and b+c > a and a+c >b

    def perimeter(self):
        '''计算周长'''
        return self.a+self.b+self.c

def main():
    a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main()




