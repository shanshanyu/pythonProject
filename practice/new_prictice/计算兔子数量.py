'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
'''
小兔子   中兔子   老兔子
1        0        0
0        1        0
1        0        1
1        1        1

小兔子=中兔子+老兔子
中兔子 = 小兔子
老兔子 = 中兔子
'''


def count_rabbit(n):
    for i in range(1,n+1):
        if i == 1:
            x = 1
            y = 0
            z = 0
        elif i == 2:
            x = 0
            y = 1
            z = 0
        else:
            z = z + y
            y = x
            x = y + z -x

        print(x+y+z)




if __name__ == '__main__':
    month = int(input('输入月份: '))
    count_rabbit(month)
