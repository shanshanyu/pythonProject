'''
create_time: 2024/6/13 10:58
author: yss
version: 1.0
'''

import itertools


def main():
    count = 0
    # 全排列
    a = itertools.permutations('ABCD')
    for _ in a:
        count += 1
        print(_)
    print(count)


if __name__ == '__main__':
    main()