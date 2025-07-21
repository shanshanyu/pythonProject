'''求两个数的最大公约数'''


def hcf(a,b):
    for i in range(a,0,-1):
        if a % i == 0 and b % i == 0:
            return i



if __name__ == '__main__':
    a = int(input('a= '))
    b = int(input('b= '))
    print(hcf(a,b))