'''
create_time: 2023/6/8 15:58
author: yss
version: 1.0
'''

def get_prime(start,end):
    for i in range(start,end+1):
        flag = True
        for j in range(2,int(i/2)):      #for(i = 2; i < j/2;i++)
            if i % j == 0:
                flag = False
                break

        if flag:
            print(i,'is primer')


if __name__ == '__main__':
    get_prime(30000000,30000200)
