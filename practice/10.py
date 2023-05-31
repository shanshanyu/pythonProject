'''
create_time: 2023/5/30 20:18
author: yss
version: 1.0
'''

#mini计算器

#eval 计算表达式

def calc():
    num1 = input('请输入第一个整数：')
    num2 = input('请输入第二个整数：')
    op = input('请输入运算符：')
    expression = num1 + op + num2
    print(eval(expression)) #直接打印不返回了

calc()
