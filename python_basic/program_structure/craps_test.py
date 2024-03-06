'''
create_time: 2024/3/5 16:30
author: yss
version: 1.0
'''
import random

money = 1000

while money > 0:
    print(f'您当前的资产为{money}')

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
        while True:
            current = random.randint(1,6) + random.randint(1,6)
            print(f'玩家摇出的点数是 {current}')
            if current == 7:
                money -= debt
                print('庄家胜')
                break
            elif current == first:
                money += debt
                print('玩家胜')
                break
            else:
                pass


print(f'你破产了，当前的money为 {money}')