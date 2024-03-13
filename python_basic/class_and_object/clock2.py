'''
create_time: 2024/3/8 11:10
author: yss
version: 1.0

定义一个类描述数字时钟   xx:xx:xx

定义一个类，类中的属性包含小时，分钟，秒，一个打印时间的方法，一个走秒的方法->创建一个对象，传入当前时间，然后走秒，打印
'''
import time


class Clock(object):
    '''
    数字时钟类
    '''
    def __init__(self,hour,minute,second):
        '''
        初始化数字时钟类
        :param hour: 小时
        :param minute: 分钟
        :param second: 秒数
        '''
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        '''
        显示当前时钟
        :return:
        '''
        print(f'当前时间是 {self.hour}:{self.minute}:{self.second}')

    def run(self):
        '''走秒
        这个分支语句可以精简，minute 的正在是在 second 增加的基础上才会发生的，所以 minute 的判断可以放到 second 判断下面
        '''
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        if self.hour == 24:
            self.hour = 0

def main():
    cur_time = time.localtime()
    c = Clock(cur_time.tm_hour,cur_time.tm_min,cur_time.tm_sec)
    while True:
        #打印时间
        c.show()
        #暂停1s
        time.sleep(1)
        #走秒
        c.run()

if __name__ == '__main__':
    main()

