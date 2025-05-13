'''
打印水仙花数

其各位数字立方和等于该数本身
'''



def narcissus(num):
    a = int(num/100)
    b = int(num/10%10)
    c = num%10
    if num == a**3 + b**3 + c**3:
        return True


def main():
    for i in range(100,999):
        if narcissus(i):
            print(i)


if __name__ == '__main__':

    main()