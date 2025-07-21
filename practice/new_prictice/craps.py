'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：
玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，
如果玩家摇出了 7 点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）
'''
import random


def craps():
    money = 1000
    while money:
        print(f'当前本金：{money}')

        while True:
            wagered = int(input('请下注：'))
            if 0 < wagered <= money:
                break
            else:
                print('输入有误，请重新下注！')

        #开始游戏
        choice = random.randint(2, 12)
        print(f'本轮摇出的点数是: {choice}')
        if choice == 7 or choice == 11:
            print('本局玩家获胜')
            money += wagered
            continue   #这个continue 不需要，不会再走到其他分支了，直接回到上面的for循环了
        elif choice == 2 or choice == 3 or choice == 12:
            print('本局庄家获胜')
            money -= wagered
            continue   #这个continue 不需要，不会再走到其他分支了，直接回到上面的for循环了
        else:
            while True:
                next_choice = random.randint(2, 12)
                print(f'本轮摇出的点数是: {next_choice}')
                if next_choice == 7:
                    print('本局庄家获胜')
                    money -= wagered
                    break
                elif next_choice == choice:
                    print('本局玩家获胜')
                    money += wagered
                    break
                else:   #这个 else 也不用了，加不加这个都是回到上面的 while True
                    continue
    print('你破产了, 游戏结束!')



if __name__ == '__main__':
    craps()



