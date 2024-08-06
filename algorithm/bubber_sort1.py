'''
create_time: 2023/6/15 16:57
author: yss
version: 1.0
'''


lst = [5,4,3,2,1,6,7,8,10,9]

len_lst = len(lst)

i = 0
while i < len_lst-1:  #冒泡排序   循环次数  n 个数循环 n-1 次就够了
    j = 0
    while j < len_lst-i-1:
        if lst[j] > lst[j+1]:
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp
        j += 1
    i += 1


for i in lst:
    print(i)