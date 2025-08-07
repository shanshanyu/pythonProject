from enum import Enum
import random

class Suite(Enum):
    SPADE,HEART,CLUB,DIAMOND = range(4)


class Card:
    '''牌'''
    def __init__(self,suite,face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return f'{suites[self.suite.value]}{faces[self.face]}' #返回牌的花色和点数

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

class Poker:
    '''一副扑克'''
    def __init__(self):
        self.cards = [Card(i,j) for i in Suite for j in range(1,14)]
        self.current = 0 #发牌位置

    def shuffle(self):
        '''洗牌'''
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        '''发牌'''
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        return self.current < len(self.cards)


class Player:
    '''玩家'''
    def __init__(self,name):
        self.name = name
        self.cards = [] #玩家手上的牌

    def get_one(self,card):
        '''玩家摸牌'''
        self.cards.append(card)

    def arrange(self):
        '''整理牌'''
        self.cards.sort()

def main():
    p = Poker()  #创建一副牌
    p.shuffle()  #洗牌
    players = [Player('东邪'),Player('西毒'),Player('南帝'),Player('北丐')]
    #将牌发到玩家手上
    for _ in range(13):
        for player in players:
            player.get_one(p.deal())

    #玩家整理手上的牌
    for player in players:
        player.arrange()
        print(f'{player.name}: ',end='')
        print(player.cards)


if __name__ == '__main__':
    main()
    print(Suite.SPADE.value)


#列表生成式
# a = [i*j for i in range(1,4) for j in range(1,4)]
# print(a)





