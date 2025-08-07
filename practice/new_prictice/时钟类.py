'''数字时钟'''
import time


class Clock(object):
    '''时钟对象初始化'''
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    '''走字'''
    def run(self):
        self.second = self.second + 1
        if self.second == 60:
            self.second = 0
            self.minute +=1
        if self.minute == 60:
            self.minute = 0
            self.hour +=1
        if self.hour == 24:
            self.hour = 0

    def show(self):
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'


def main():
    clock = Clock()
    while True:
        print(clock.show())
        clock.run()
        time.sleep(1)


if __name__ == '__main__':
    main()

