'''
create_time: 2023/11/7 10:56
author: yss
version: 1.0
创建一个时钟类，每秒钟打印一下时间
'''

import time

class Clock(object):
    def __init__(self,hour,minutes,seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def show(self):
        print(f"当前时间  {self.hour}:{self.minutes}:{self.seconds}")

    def run(self):
        while True:
            self.seconds += 1
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0

            if self.minutes == 60:
                self.hour += 1
                self.minutes = 0

            if self.hour == 24:
                self.hour = 0

            self.show()
            time.sleep(1)


if __name__ == '__main__':
    c = Clock(12,11,13)
    c.run()
