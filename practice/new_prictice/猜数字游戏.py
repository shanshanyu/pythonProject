'''猜数字游戏'''
import random


def guess_num():
    answer = random.randint(1,100)
    count = 0
    while True:
        print('猜数字游戏开始')
        a = int(input('请输入你猜测的数字：'))
        count += 1
        if a == answer:
            print('你猜对了')
            print(f'你一共猜了{count}次')
            break
        elif a < answer:
            print('小了')
        else:
            print('大了')


if __name__ == '__main__':
    guess_num()