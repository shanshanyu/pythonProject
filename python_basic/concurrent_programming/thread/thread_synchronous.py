'''
create_time: 2023/6/8 18:02
author: yss
version: 1.0
'''
import threading
import time


class Account(object):   #典型的线程安全类，构造方法初始化锁，需要保证线程安全的方法  加锁  解锁
    def __init__(self,account_no,money):
        self.__account_no = account_no  #将实例属性隐藏，避免外部直接访问
        self.__money = money

        self.lock = threading.RLock()

    def get_money(self):
        return self.__money

    def draw(self,draw_mount):  #这个方法存在共享资源 self.__money，需要线程同步
        self.lock.acquire()  #加锁
        try:
            if self.__money >= draw_mount:
                time.sleep(0.1)
                self.__money -= draw_mount
                print(f'成功取出{draw_mount}')
            else:
                print('余额不足')
        finally:
            self.lock.release()  #释放锁

if __name__ == '__main__':
    a = Account('1234',500)  #存钱

    t1 = threading.Thread(target=a.draw,name='thread1',args=(500,))
    t2 = threading.Thread(target=a.draw, name='thread2', args=(500,))
    t1.start()
    t2.start()
    #a.draw(500)
    time.sleep(1)
    print('当前余额:{}'.format(a.get_money()))
