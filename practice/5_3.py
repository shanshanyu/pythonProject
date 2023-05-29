'''
create_time: 2023/5/29 20:58
author: yss
version: 1.0
'''
#猜数字游戏
import random
print('猜数字游戏,数字在 1~100 之间')
print('-'*100)
num = random.randint(1,100)
for i in range(1,11):
    try:
        input_num = int(input('请输出一个数字：'))
    except:
        print('你输入的不是一个数字，请继续！')
        continue

    if input_num < num:
        print('小了')
    elif input_num > num:
        print('大了')
    else:
        print('恭喜你猜对了')
        print(f'使用了{i}次机会')
        break

if i < 3:
    print('大聪明一枚')
elif i < 7:
    print('马马虎虎')
elif i < 10:
    print('有点小笨')
else:
    print('蠢逼')