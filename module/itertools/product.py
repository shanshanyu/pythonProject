'''
create_time: 2024/6/13 17:57
author: yss
version: 1.0
'''

import itertools


def main():
    a = itertools.product('ABCD','1234')
    for i in a:
        print(i)


if __name__ == '__main__':
    main()