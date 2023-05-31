'''
create_time: 2023/5/30 19:23
author: yss
version: 1.0
'''

#元组遍历
coffe_name = ('蓝山','卡布奇洛','拿铁')

for i in range(len(coffe_name)):  #可迭代对象同时用到了索引，可以考虑用 enumerate 函数
    print(i+1,coffe_name[i])

num = input('请输入coffee编号：')
print(f'{coffe_name[int(num)-1]}')


for i,val in enumerate(coffe_name):
    print(i+1,coffe_name[i])

