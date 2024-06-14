'''
create_time: 2024/6/13 17:33
author: yss
version: 1.0
'''

import itertools


def main():
    # 从ABCD中选出2个
    a = itertools.combinations('ABCD',2)
    for _ in a:
        print(_)


if __name__ == '__main__':
    main()