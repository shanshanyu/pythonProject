'''
create_time: 2023/11/7 14:35
author: yss
version: 1.0
'''
import time

class Clock(object):
    def __init__(self,hour,minutes,seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def now(cls):
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

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

    c = Clock.now()
    c.run()