'''
create_time: 2024/3/5 16:01
author: yss
version: 1.0
'''
#双骰游戏


'''
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，
庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。

玩家下注
比点数

'''

'''
整个程序的结构是：
while:
  if:
  else if:
  else:
    继续循环，不好再写在 else 代码块内
'''

import random

money = 1000

while money > 0:
    print(f'您当前的资产为{money}')
    need_go_on = False  #是否继续游戏

    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break

    first = random.randint(1,6) + random.randint(1,6)  #玩家第一次摇出的点数
    print(f'玩家第一次摇出的点数为{first}')
    if first == 7 or first == 11:
        money += debt
        print('玩家胜')
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('庄家胜')
    else:
        need_go_on = True  #通过一个标志继续执行下面的循环

    while need_go_on:
        need_go_on = False
        current = random.randint(1,6) + random.randint(1,6)
        print(f'玩家摇出的点数是 {current}')
        if current == 7:
            money -= debt
            print('庄家胜')
        elif current == first:
            money += debt
            print('玩家胜')
        else:
            need_go_on = True  #通过一个标志继续执行下面的循环

print(f'你破产了，当前的money为 {money}')




