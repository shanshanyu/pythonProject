'''
create_time: 2023/6/17 16:49
author: yss
version: 1.0
'''
lst = []

for i in range(300):
    lst.append(i)


def test(lst):
    print(lst)

test(lst[:int(len(lst)/3)])   #列表切片
test(lst[int(len(lst)/3):int(len(lst)/3*2)])
test(lst[int(len(lst)/3*2):])

print(lst)