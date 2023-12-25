'''
create_time: 2023/11/16 14:04
author: yss
version: 1.0
'''
import time


def main():
    try:
        with open('test.txt','r') as f:
            #用 for..in 循环按行读取
            for line in f:
                print(line,end='')
                time.sleep(1)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()