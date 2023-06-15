# 2023/6/14 20:23
import threading

a = 3
def test():
    print(a)  #函数内可以访问全局变量，如果要修改全局变量，需要加上 global a

test()

num = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def run(self):
        global num
        with mutex:
            for i in range(1000000):
                num += 1   #这里修改全局变量 num 的值，需要 global 声明
            print(num)


thread_list = []
for i in range(5):
    t = MyThread()
    t.start()
    thread_list.append(t)

for thread in thread_list:
    thread.join()
