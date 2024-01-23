'''
create_time: 2023/3/29 21:30
author: yss
version: 1.0
'''

a = 'tom'
b = a
#获取变量的地址
print(id(a))
print(id(b))

#获取变量的类型
print(type(a))

#获取变量的值
print(a)

a = 'jerry'
print(id(a))  #a 的引用变了
print(id(b))  #b 的引用没变



#变量作用域
def test():
    a = 4  # a 是局部变量   如果需要访问全局变量： global  a   声明 a 是全局变量
    print('local var: ',locals())
    print('global var: ',globals())

test()
print(a)

name = 'jerry'
class Student():
    name = 'tom'
    print(name)
    print('student global',globals())
    print('student local',locals())

b = Student()

print(name)