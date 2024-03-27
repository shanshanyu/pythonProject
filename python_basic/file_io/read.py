'''
create_time: 2024/3/27 17:11
author: yss
version: 1.0
'''


def main():
    f = open('./test.txt','r')
    data = f.read()
    print(data, type(data))

if __name__ == '__main__':
    main()