'''
判断101-200之间有多少个素数,直接输出
'''
import math


def is_prime(num):
    '''计算素数(质数)的标准方式'''
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True





def print_prime():
    for i in range(100,201):
        ret = is_prime(i)
        if ret:
            print(i)


if __name__ == '__main__':
    print_prime()