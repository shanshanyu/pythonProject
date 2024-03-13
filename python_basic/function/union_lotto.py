'''
create_time: 2024/3/7 18:11
author: yss
version: 1.0

双色球玩法
可以选择多注
从33个数中选择6个数->从16个数中选择1个数->打印选择的数
'''
import random


def display(balls):
    for i in balls:
        print('%02d' % i,end=' ')

def union_lotto():
    red_balls = [x for x in range(1,34)]
    select_balls = random.sample(red_balls,k=6)  #从33个数中不重复的选择6个数
    select_balls.sort()  #排序
    select_balls.append(random.randint(1,16))  #从16个数中选择1个数
    return select_balls

def main():
    balls = union_lotto()
    display(balls)


if __name__ == '__main__':
    main()