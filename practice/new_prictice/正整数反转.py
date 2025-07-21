'''将一个数反转'''

def reverse_num(n):
    if n <= 0:
        return -1  #输入有误，返回-1
    res = 0
    while n > 0:
        res = res*10 + n%10  #把最后一位取出来
        n = n // 10
    return res


if __name__ == '__main__':
    num = int(input("输入一个正整数："))
    ret = reverse_num(num)
    if ret == -1:
        print('输入有误')
    else:
        print(ret)