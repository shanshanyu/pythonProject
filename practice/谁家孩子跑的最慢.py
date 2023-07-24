'''
create_time: 2023/7/17 17:04
author: yss
version: 1.0

假设有张、王、李三家，每家都有3个孩子。某一天，这三家的9个 孩子一起短跑比赛，规定不考虑年龄大小，第一名得9分，第二名得8 分，第三名得7分，
以此类推。比赛结束后统计分数发现三家孩子的总 分是相同的，同时限定这9个孩子的名次不存在并列的情况，且同一家 的孩子不会获得相连的名次。
现已知获得第一名的是李家的孩子，获得 第二名的是王家的孩子，要求编程求出获得最后一名的是哪家的孩子。
'''

#7 个数字分 3 份怎么分？每一份中不能出现相连的数字
#第三名只能是张家的，那就变成了6个数字分3份

#遍历3个数组，第一个数组因为不能连续，不到 6，最后一个数组不能超过 15，所以也不能到 6

score = []
for i in range(3):
    lst = []
    for j in range(3):
        lst.append(0)
    score.append(lst)

#print(score)  初始化列表
score[0][0] = 7
score[1][0] = 8
score[2][0] = 9

for x in range(4,6):
    for y in range(4,7):
        for z in range(4,6):
            if x != y and y != z and x != z and 15-x-score[0][0] != 15-y-score[1][0] and 15-x-score[0][0] != 15-z-score[2][0] and 15-y-score[1][0] != 15-z-score[2][0]:
                score[0][1] = x
                score[1][1] = y
                score[2][1] = z
                score[0][2] = 15-x-7
                score[1][2] = 15-y-8
                score[2][2] = 15-z-9
                print(score)


