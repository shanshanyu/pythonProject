'''输入三个整数x,y,z，请把这三个数由小到大输出。'''
def print_num():
    '''直接放到列表里面，然后排序就完事了'''
    x = int(input())
    y = int(input())
    z = int(input())

    if x > z:
        x,z = z,x
    if x > y:
        x,y = y,x
    if y > z:
        y,z = z,y

    print(x,y,z)


if __name__ == '__main__':
    print_num()