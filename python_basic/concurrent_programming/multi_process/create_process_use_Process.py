'''
create_time: 2024/4/23 11:02
author: yss
version: 1.0
'''
import multiprocessing


def _99table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j}',end='\t')
        print()
    print('')


def main():
    p = multiprocessing.Process(target=_99table,name='new process')  # 直接调用 multiprocessing.Process 创建对象
    p.start()
    p.join()
    print('father process over')


if __name__ == '__main__':
    main()
