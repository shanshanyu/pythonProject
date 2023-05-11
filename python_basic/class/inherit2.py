'''
create_time: 2023/4/18 16:32
author: yss
version: 1.0
'''

class Bird:
    def play(self):
        print("我能再天上飞")

class Ostrich(Bird):
    def play(self):
        print("我只能在地上跑")
        Bird.play(self)


a = Ostrich()
a.play()