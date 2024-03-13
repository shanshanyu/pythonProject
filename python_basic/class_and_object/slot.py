'''
create_time: 2024/3/8 14:54
author: yss
version: 1.0

python是动态语言，通过 __slot__ 属性限制实例只能有某些属性和方法
'''

class Student(object):
    '''
    学生类
    '''
    __slots__ = ('_name','_age')

    def __init__(self,name,age):
        self._name =name
        self._age = age

    #通过装饰器来修饰属性
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age

    def get_age(self):
        return self._age
    def set_age(self,age):
        self._age = age


    def play(self):
        if self.age >= 18:
            print(f'{self.name} 正在看小电影')
        else:
            print(f'{self.name} 正在学习')

def main():
    s = Student('zhangsan',19)
    s.play()
    # s.area = 'anhui'
    #用了 __slot__ 属性，不能添加其他的属性了
if __name__ == '__main__':
    main()

