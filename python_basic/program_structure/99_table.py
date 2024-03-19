'''
create_time: 2024/3/5 15:35
author: yss
version: 1.0
'''
#9*9 乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    print('')
