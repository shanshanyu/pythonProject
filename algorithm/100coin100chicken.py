'''
create_time: 2023/6/15 15:25
author: yss
version: 1.0
'''

#百钱百鸡   一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱，现 在要用百钱买百鸡，请问公鸡、母鸡、小鸡各多少只

for x in range(0,20):
    for y in range(0,34):
        for z in range(0,101):
            if 5*x+3*y+(1/3)*z == 100 and x+y+z == 100:
                print('公鸡',x)
                print('母鸡', y)
                print('小鸡', z)
                print('*'*60)


print('='*100)

