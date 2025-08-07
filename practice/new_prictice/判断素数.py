'''判断素数'''



def is_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num/2+1)):
        if num % i == 0:
            return False
    return True




if __name__ == '__main__':
    num = int(input('请输入一个数字： '))
    ret = is_primer(num)
    if ret:
        print(f'{num} 是素数')
    else:
        print(f'{num} 不是素数')

