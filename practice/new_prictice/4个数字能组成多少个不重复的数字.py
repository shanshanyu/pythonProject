# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

def print_num():
    '''输入一个列表，列表里面包含4位数字'''
    '''逆向四位，正向的不好计算，可以算出全部，然后去掉不符合条件的'''
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i!=j) and (i != k) != (j != k):
                    print('%d%d%d' % (i,j,k))



if __name__ == '__main__':
    print_num()