# 2023/6/7 20:25
import threading


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.i = 0

    def run(self):  #重写父类的 run 方法
        while self.i < 100:
            print(self.name,self.i)
            self.i += 1

t1 = MyThread()
t1.start()
for i in range(100):
    print(threading.current_thread().name,i)

