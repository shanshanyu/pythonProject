'''
create_time: 2024/4/23 11:14
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


class MyProcess(multiprocessing.Process):  # 继承 multiprocessing.Process
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        _99table()


def main():
    p = MyProcess()
    p.start()


if __name__ == '__main__':
    main()