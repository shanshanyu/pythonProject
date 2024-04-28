'''
create_time: 2024/4/23 14:55
author: yss
version: 1.0

desc: 100 个人同时像某个账户里面存 1 元
'''
import threading
import time


class Account(object):
    def __init__(self):
        self._lock = threading.Lock()
        self._account = 0

    def deposit(self,money):
        self._lock.acquire()
        try:
            new_money = self._account + money
            time.sleep(0.001)
            self._account = new_money
        finally:
            self._lock.release()

    @property
    def account(self):
        return self._account


class DepositThread(threading.Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    threads = []  # 存放线程对象的列表

    account = Account()
    for _ in range(100):
        t = DepositThread(account,1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(account.account)


if __name__ == '__main__':
    main()