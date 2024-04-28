
# 2023/6/7 20:12
import threading


def thread_func(*args,**args1):
    print(args,type(args))
    print(args1,type(args1))
    print('i am thread')
    for i in range(100):
        print(threading.current_thread().name,i)

t1 = threading.Thread(target=thread_func,args=(1,2,3),kwargs={'a':1,'b':2})  #使用 Thread类的构造器
t1.start()
for i in range(100):
    #print(threading.current_thread().getName(), i)   #getName deprecated
    print(threading.current_thread().name, i)



