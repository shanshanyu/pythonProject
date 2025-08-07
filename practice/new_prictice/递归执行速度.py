'''利用斐波那契数查看递归速度'''

import time

def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)

def fib1(n):
    if n in (0, 1):
        return 1
    a,b=1,1
    for _ in range(n):
        a,b = b,a+b
    return a

def main():
    start_time = time.time()
    for i in range(50):
        print(fib1(i))
    end_time = time.time()
    print('%.5f' % (end_time - start_time))


if __name__ == '__main__':
    main()


