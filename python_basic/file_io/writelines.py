'''
create_time: 2023/5/28 08:15
author: yss
version: 1.0
'''

#writelines 向文件中输入字符串，参数是一个可迭代对象，可以是字符串，可以是列表，如果是列表，列表的元素需要是字符串 !!!

#a = ['1','2','3',['1']]    #报错
a = ['1','2','3']
b = [1,2,3]
with open('test.txt', 'w', encoding='utf-8') as file:
    file.writelines('abcd')   #writelines 的参数是一个列表  readlines 的返回值是一个列表
    file.writelines(a)   #ok
    #file.writelines(b) error #参数是一个可迭代对象，但是对象里面的值必须是 str
    #参数是一个字符串也可以,参数需要是一个可迭代对象


with open('test.txt', 'r', encoding='utf-8') as file:   #with不是一个代码块，with 中定义的 b 在，with 语句后还可以使用
    b = file.read()

print(b)


for i in range(5):
    c = 3
    print(i)

print(i)
print(c)

def test():
    d = 4  #函数内部的是局部变量，函数外部的都是全局变量，for语句中的变量也是全局变量
    print('global',globals())
    print('local',locals())

#print(d)
test()