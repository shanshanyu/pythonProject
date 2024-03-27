'''
create_time: 2024/3/26 17:33
author: yss
version: 1.0

desc: 奥特曼打小怪兽翻新版


奥特曼和小怪兽都应该有的属性和方法：
名字
血量
攻击（方法）

奥特曼特有的属性：
魔法值
大招攻击
魔法攻击


游戏的流程：
回合制游戏，直到有一方倒下->奥特曼每次根据随机值选择攻击方式->攻击完成后怪兽没有死亡再攻击奥特曼->奥特曼恢复魔法值->继续下一步
随机值：
0~6 普通攻击
7~9 大招攻击
10  魔法攻击


奥特曼 普通攻击每次 15~25
      大招攻击如果魔法值大于等于50，消耗50点魔法值，打掉50滴血，如果小于50就打掉3/4，如果魔法值小于50，就只能使用普通攻击
      魔法攻击，攻击一群，要求魔法值 >=20，消耗20点魔法值，攻击 10~15

      魔法值每次恢复 1~10 点

怪兽  普通攻击每次 10~15


'''

from abc import ABC,abstractmethod
import random


class Fight(ABC):
    __slots__ = ('_hp','_name')
    '''
    战斗者
    '''
    def __init__(self,hp,name):
        '''hp属性的初始化'''
        self._hp = hp
        self._name = name

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp = hp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @abstractmethod
    def attack(self,other):
        pass

    def is_alive(self):
        '''
        判断是否存活应该是怪兽和奥特曼都有的方法
        :return:
        '''
        return self.hp > 0


class Ultraman(Fight):
    __slots__ = ('_hp','_mp','_name')
    def __init__(self,hp,mp,name):
        super().__init__(hp,name)
        self._mp = mp

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self,mp):
        self._mp = mp

    def attack(self,other):
        '''
        奥特曼的普通攻击
        :param other:
        :return:
        '''
        injury = random.randint(15,25)
        other.hp -= injury
        if other.hp < 0:
            other.hp = 0

    def huge_attack(self,other):
        '''
        大招攻击如果魔法值大于等于50，消耗50点魔法值
        如果血量大于50，打掉50滴血，如果小于50就打掉3/4，如果魔法值小于50，就只能使用普通攻击
        :param other:
        :return:
        '''
        if self.mp >= 50:
            #如果怪兽的血量大于50就减去50，如果小于50就减去 3/4
            injury = 50 if other.hp > 50 else other.hp*3/4
            other.hp -= injury
            if other.hp < 0:
                other.hp = 0
        else:
            #使用普通攻击
            self.attack(other)

    def magic_attack(self,others):
        '''
        魔法攻击，攻击一群，要求魔法值 >=20，消耗20点魔法值，攻击 10~15
        :param others:
        :return:
        '''
        if self.mp >= 20:
            for monster in others:
                if monster.is_alive():
                    monster.hp -= random.randint(10,15)
                    if monster.hp < 0:
                        monster.hp = 0
            return True
        else:
            return False

    def resume(self):
        '''
        奥特曼恢复魔法值
        :return:
        '''
        self.mp += random.randint(1,10)

    def __str__(self):
        return f'奥特曼 {self.name} 还有 {self.hp} 血，还有 {self.mp} 魔法值'


class Monster(Fight):
    __slots__ = ('_hp','_name')
    def attack(self,other):
        injury = random.randint(10,15)
        other.hp -= injury
        if other.hp < 0:
            other.hp = 0

    def __str__(self):
        return f'小怪兽 {self.name} 还有 {self.hp} 血'


def is_any_alive(others):
    '''
    判断是否有怪兽存活
    :param others:
    :return:
    '''
    for monster in others:
        if monster.hp > 0:  #对怪兽列表进行判断
            return True
    else:
        return False


def select_alive_one(others):
    '''
    从一堆小怪兽中选出一只活着的
    :param others:
    :return:
    '''
    while True:
        length = len(others)
        index = random.randrange(length)
        monster = others[index]
        if monster.is_alive():
            return monster


def main():
    u1 = Ultraman(100,100,'迪迦')  #一个奥特曼，三只小怪兽
    m1 = Monster(75,'m1')
    m2 = Monster(50,'m2')
    m3 = Monster(25,'m3')

    m_list = [m1,m2,m3]  #怪兽列表
    #攻击轮次
    rack_round = 1

    while u1.is_alive() and is_any_alive(m_list):
        #循环终止条件是有一方倒下
        skill = random.randint(1,10)
        if skill <= 6:
            #普通攻击
            monster = select_alive_one(m_list)
            u1.attack(monster)
        elif skill <= 9:
            #大招攻击
            monster = select_alive_one(m_list)
            u1.huge_attack(monster)
        else:
            #范围攻击
            u1.magic_attack(m_list)

        #如果小怪兽有存活，小怪兽攻击奥特曼
        if is_any_alive(m_list):
            monster = select_alive_one(m_list)
            monster.attack(u1)

        #一轮攻击过后，打印奥特曼和小怪兽的情况
        print(f'第 {rack_round} 轮攻击过后')
        print(u1)
        for monster in m_list:
            print(monster)

        #攻击轮次加1
        rack_round += 1

        #奥特曼恢复魔法值
        u1.resume()

    if u1.is_alive():
        print('奥特曼获胜')
    else:
        print('小怪兽获胜')


if __name__ == '__main__':
    main()