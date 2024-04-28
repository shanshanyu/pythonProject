'''
create_time: 2024/4/24 11:50
author: yss
version: 1.0

desc: 1~10000000 的累加，计算耗时
'''
import time


def main():
    start = time.time()
    res = 0
    for i in range(100000000):
        res += i
    print(res)
    end = time.time()
    print('耗时：%.2f' % (end-start))


if __name__ == '__main__':
    main()
