'''
create_time: 2023/5/29 17:56
author: yss
version: 1.0
'''

#商品加个竞猜
import random

print('竞猜产品为小米机器人：价格 【1000-1500】之间')

price = random.randint(1000,1500)
while True:
    input_price = int(input('输入价格：'))
    if input_price < price:
        print('小了')
    elif input_price > price:
        print('大了')
    else:
        print('答对了')
        break
