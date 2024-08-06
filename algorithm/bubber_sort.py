'''
create_time: 2023/6/15 16:38
author: yss
version: 1.0
'''


lst = [5,4,3,2,1,6,7,8,10,9]

#对 lst 进行冒泡排序，不使用列表的排序功能

lst_len = len(lst)
for i in range(lst_len):  # 控制循环次数
    for j in range(lst_len-i-1):  #每次循环把最大的数放到最后
        if lst[j] > lst[j+1]:
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp

for i in lst:
    print(i)
