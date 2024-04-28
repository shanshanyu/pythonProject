'''
create_time: 2024/4/22 15:21
author: yss
version: 1.0

'''


import threading


def print_i(val):
    for i in range(1,val):
        print(threading.current_thread().name,i)


class Mythread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print_i(5)


if __name__ == '__main__':
    t = Mythread()
    t.start()