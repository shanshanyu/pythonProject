'''
斐波那契数列输出
'''

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    fib_list = []
    for i in range(0,10):
        fib_list.append(fibonacci(i))
    print(fib_list)
