'''
create_time: 2023/6/8 16:59
author: yss
version: 1.0
'''


import threading
import time


def hello():
    print('hello')

t = threading.Thread(target=hello)
t.start()

while t.is_alive():
    time.sleep(1)

t.start()