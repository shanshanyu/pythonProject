'''
输出 9*9 乘法口诀表
'''
def print_99():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={str(i*j)}'+' ',end='')
        print()


if __name__ == '__main__':
    print_99()