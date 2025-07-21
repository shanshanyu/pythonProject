'''打印100以内的素数'''


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2+1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(100):
        if is_prime(i):
            print(i)