'''
create_time: 2023/6/15 14:29
author: yss
version: 1.0
'''

# 兔子产子  有一对兔子，从出生后的第3个月起每个月都生一对兔子。小兔子 长到第3个月后每个月又生一对兔子，假设所有的兔子都不死，问30个 月内每个月的兔子总对数为多少
# 画出一个每个月的兔子表
'''
；小兔子对数  等于  上一个老兔子对数+上一个中兔子对数
；中兔子对数  等于  上一个小兔子对数
；老兔子对数  等于  上一个中兔子对数+上一个老兔子对数
'''
# 用自己的话表述
# 伪代码  用递归解决

def rabbit_all(num): # 封闭函数
    def rabbit_small(num):  # 局部函数
        if num == 1:
            return 1
        return rabbit_big(num-1) + rabbit_medium(num-1)

    def rabbit_medium(num):
        if num == 1:
            return 0
        return rabbit_small(num-1)

    def rabbit_big(num):
        if num == 1:
            return 0
        return rabbit_medium(num-1)+rabbit_big(num-1)

    return rabbit_big(num) + rabbit_medium(num) + rabbit_small(num)

if __name__ == '__main__':
    for i in range(1,31):
        print(f'第{i}个月的总兔子对数为{rabbit_all(i)}')   #1   1  2  3  5  8   fibonacci 序列
