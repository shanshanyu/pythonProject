'''
create_time: 2023/11/16 14:08
author: yss
version: 1.0
'''
import time


def main():
    try:
        with open('test.txt','r') as f:
            #readliens 把文件读到列表里面
            lst = f.readlines()
            print(type(lst))
            print(lst)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()