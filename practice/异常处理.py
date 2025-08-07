

class InputError(ValueError):
    pass

def fib(n):
    if n < 0:
        raise(InputError('输入有误，小于0'))
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)


def main():
    flag = True
    while flag:
        num = int(input('输入一个整数：'))
        try:
            ret = fib(num)
            print(f'fib{num}={ret}')
        except InputError as err:
            print(err)
            flag = False



if __name__ == '__main__':
    main()