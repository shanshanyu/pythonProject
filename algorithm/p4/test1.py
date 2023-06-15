'''
create_time: 2023/6/15 16:05
author: yss
version: 1.0
'''

#百钱百鸡问题
for x in range(0,20):
    for y in range(0,34):
        z = 100-x-y
        if 5*x+3*y+z/3 == 100 and x+y+z == 100:  #x 和 y 确定了，z 也就确定了，不用再循环 z 了，时间复杂度降低了一个量级
            print('公鸡', x)
            print('母鸡', y)
            print('小鸡', z)
            print('*' * 60)