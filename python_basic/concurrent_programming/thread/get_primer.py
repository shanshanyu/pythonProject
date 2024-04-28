'''
create_time: 2023/6/8 15:58
author: yss
version: 1.0
'''


def get_prime(start,end):
    for i in range(start,end+1):
        if i <= 1:
            continue

        flag = True
        for j in range(2,int(i/2)+1):      #for(i = 2; i < j/2;i++)
            '''这个质数的判断逻辑有问题，4 判断错误，应该改成 
            for j in range(2,int(i/2)+1)  原：for j in range(2,int(i/2))
            这个质数的判断逻辑还有其他问题，小于 3 的数会判断错误
            '''
            if i % j == 0:
                flag = False
                break

        if flag:
            print(i,'is primer')


if __name__ == '__main__':
    get_prime(1,6)
