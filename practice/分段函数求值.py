'''分段函数求值'''

x = float(input('请输入x值: '))
if x > 1:
    y = 3*x-5
elif x >= -1: #这里面包含了 <=1
    y = x+2
elif x < -1:
    y = 5*x+3

print('y=%.1f' % y)