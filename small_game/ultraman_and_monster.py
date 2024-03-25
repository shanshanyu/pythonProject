'''
create_time: 2023/11/7 16:50
author: yss
version: 1.0


'''
import random
from abc import ABCMeta,abstractmethod


class Fighter(metaclass=ABCMeta):   #抽象基类
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        self._name = name
        self._hp = hp

    @property  #用property修饰方法，把方法变成属性
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp

    @property
    def alive(self):
        '''
        判断是否存活
        :return:
        '''
        return self._hp > 0

    @abstractmethod
    def attack(self,other):  #other表示被攻击的对象
        ''''
        攻击
        '''
        pass


class Ultraman(Fighter):
    __slots__ = ['_name','_hp','_mp']
    '''
    hp:血量
    mp：魔法值
    '''

    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self,mp):
        self._mp  = mp

    def attack(self,other):
        #普通攻击
        other.hp -= random.randint(15,25)


    def huge_attack(self,other):
        '''
        究极必杀技
        如果魔法值大于等于50，消耗50点魔法值，打掉50滴血，如果小于50就打掉3/4
        如果魔法值小于50，就只能使用普通攻击
        :param other: other
        :return: boolean
        '''
        if self.mp >= 50:
            self.mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury <= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)

    def magic_attck(self,others):
        '''
        魔法攻击，攻击一群
        要求魔法值 >=20
        :param others:
        :return:
        '''

        if self.mp >= 20:
            self.mp -= 20
            for tmp in others:
                if tmp.alive:
                    tmp.hp -= random.randint(10,15)
            return True
        else:
            return False

    def resume(self):
        '''
        恢复魔法值
        :return:
        '''
        incr_point = random.randint(1,10)
        self.mp += incr_point
        return incr_point

    def __str__(self):
        return f'奥特曼:{self.name},血量：{self.hp},魔法值：{self.mp}'


class Monster(Fighter):
    def __init__(self,name,hp):
        super().__init__(name,hp)

    def attack(self,other):
        other.hp -= random.randint(10,20)

    def __str__(self):
        return f'小怪兽:{self.name},血量：{self.hp}'


def is_any_alive(monsters):
    '''判断是否有小怪兽存活'''
    for monster in monsters:
        if monster.alive:
            return True
    return False


def select_alive_one(monsters):
    '''随机选取一只小怪兽'''
    length = len(monsters)
    while True:
        index = random.randrange(length)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(ultraman,monsters):
    print(ultraman)
    for monster in monsters:
        print(monster)


def main():
    u = Ultraman('迪迦', 1000, 250)
    m1 = Monster('m1', 250)
    m2 = Monster('m2', 500)
    m3 = Monster('m3', 700)
    ms = [m1, m2, m3]

    fight_round = 1
    while u.alive and is_any_alive(ms) :
        print('=========第 %2d 轮游戏开始===============' % fight_round)
        m = select_alive_one(ms)

        skill = random.randint(0,10)  # 根据随机数选择ultraman的技能
        if skill <= 6 :  # 普通攻击
            print('%s 使用了普通攻击' % u.name)
            u.attack(m)
            print('%s 的魔法值恢复了 %d 点' % (u.name, u.resume()))

        elif skill <= 9:
            if u.magic_attck(ms) :
                print('%s 使用了魔法攻击' % u.name)
            else :
                print('%s 使用魔法攻击失败' % u.name)
        else:
            if u.huge_attack(m):
                print('%s 使用了必杀技锤了 %s' % (u.name, m.name))
            else :
                print('%s 使用了普通攻击打了 %s' % (u.name, m.name))
                print('%s 的魔法值恢复了 %d 点' % (u.name, u.resume()))

        if m.alive :
            print('%s 回击了 %s' % (m.name, u.name))
            m.attack(u)

        display_info(u, ms)  # 打印奥特曼和小怪兽的信息
        fight_round += 1

    print('游戏结束！')
    if u.alive :
        print('奥特曼获胜')
    else :
        print('小怪兽获胜')

if __name__ == '__main__':
    main()











