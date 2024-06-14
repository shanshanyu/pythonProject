'''
create_time: 2024/6/14 10:29
author: yss
version: 1.0
'''
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class Account(object):
    def __init__(self,account_no,money):
        self.account_no = account_no
        self.money = money
        self._lock = threading.Lock()  # 锁对象支持with语句

    def deposit(self,money):
        '''
        存钱（需要加锁）
        :param money:
        :return:
        '''
        with self._lock:
            self.money += money


def main():
    # threads = []
    # account = Account('12345',0)
    # for i in range(100):
    #     t = threading.Thread(target=account.deposit,args=(1,))   # get thread object
    #     threads.append(t)
    #     t.start()
    #
    # for thread in threads:
    #     thread.join()
    #
    # print(account.money)

    '''
    采用线程池
    :return:
    '''
    account = Account('12345', 0)
    pool = ThreadPoolExecutor(max_workers=100)
    threads = []
    for _ in range(100):
        t = pool.submit(account.deposit,1)
        threads.append(t)
    # 关闭线程池
    pool.shutdown()

    for t in threads:
        t.result()

    print(account.money)


if __name__ == '__main__':
    main()