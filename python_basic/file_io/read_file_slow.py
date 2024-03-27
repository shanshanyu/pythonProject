'''
create_time: 2024/3/27 17:31
author: yss
version: 1.0

几种读取文件的方式
'''
import time


def main():
    with open('./test.txt','r',encoding='utf-8') as f:
        #一次读取整个文件
        data = f.read()
        print(data)

    with open('./test.txt','r',encoding='utf-8') as f:
        #一行一行读取
        for i in f:
            print(i,end='')
            time.sleep(0.5)

    with open('./test.txt', 'r', encoding='utf-8') as f :
        #一次性读取所有行
        data = f.readlines()
        print(data)


if __name__ == '__main__':
    main()