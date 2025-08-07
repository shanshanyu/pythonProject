'''双色球选号'''
import random


def double_color_balls(num=1):
    red_balls = [i for i in range(1,34)]  #红色球
    blue_balls = [j for j in range(1,17)]  #蓝色球

    for i in range(num):
        select_red = random.sample(red_balls,k=6)
        select_red.sort()
        select_blue = random.choice(blue_balls)

        select_red.append(select_blue)
        print(select_red)


def main():
    double_color_balls(3)


if __name__ == '__main__':
    main()
