'''
create_time: 2023/6/8 15:43
author: yss
version: 1.0
'''
import threading


def print_i():
    for i in range(100):
        print(threading.current_thread().name,i)
        print(threading.currentThread().name)


class MyThread(threading.Thread):  #通过继承 threading.Thread 类来创建实例
    def __init__(self):  #子类重写父类的构造方法
        super().__init__()

    def run(self):
        print_i()



if __name__ == '__main__':
    t = MyThread()
    t.name = 'new_thread'
    t.start()