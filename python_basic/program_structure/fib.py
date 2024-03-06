'''
create_time: 2024/3/5 16:44
author: yss
version: 1.0
'''


#返回斐波那契数列，从第三个数开始，每个数是之前两个数的和
def fibnaci(n):
    '''
    计算斐波那契数列
    :param n:
    :return:
    '''
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibnaci(n-1) +  fibnaci(n-2)

for i in range(1,21):
    print(fibnaci(i))
# print(fibnaci.__doc__)