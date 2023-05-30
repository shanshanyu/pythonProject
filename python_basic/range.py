# 2023/5/27  11:50

#range测试
'''
range(start,stop,step)   start 默认为 0
range(5)
range(0,5)
range(0,5,2)
'''


for i in range(5):
    print(i)

print('-'*40)

for i in range(0,5):
    print(i)

print('-'*40)

for i in range(0,5,2):
    print(i)
print('-' * 40)

for i in range(1,5,2):
    print(i)
print('-'*100)

for i in range(4,-1,-1):  #列表逆序遍历
    print(i)