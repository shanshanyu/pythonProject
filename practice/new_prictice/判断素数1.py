'''判断素数
素数的定义是什么？
大于1的正整数中，只能被1和自身整除的数？

'''

def is_primer(num:int)->bool:
    if num < 2:
        return False
    for i in range(2, int(num/2 + 1)):   # 2 3 走不到这个for 循环，直接判断为 True？
        if num % i == 0:
            return False
    return True


def main():
    for i in range(1, 100):
        if is_primer(i):
            print(i)


if __name__ == '__main__':
    main()