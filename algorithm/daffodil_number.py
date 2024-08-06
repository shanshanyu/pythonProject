'''
create_time: 2023/6/15 10:03
author: yss
version: 1.0
'''
import math
import time

# 通过车牌号抓小偷，这个问题和水仙花数问题很像

#print(math.sqrt(4))  #返回值是一个 float

start_time = time.time()

flag = False
for i in range(1000,10000):
    a1 = i // 1000
    a2 = i // 100 % 10
    a3 = i // 10 % 10
    a4 = i % 10
    if a1 == a2 and a3 == a4 and a1 != a3 and math.sqrt(i) == int(math.sqrt(i)):
        flag = True
        res = i
        break

if flag:
    print(res)
else:
    print('没找到')

end_time = time.time()

print(f'程序执行耗时：{end_time-start_time}')
