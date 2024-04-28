'''
create_time: 2023/8/30 17:05
author: yss
version: 1.0
华氏温度转换为摄氏温度
'''


f = float(input('请输入华氏温度：'))

c = (f-32)/1.8

print('对应的摄氏温度是：%0.1f' % c)
print(f'对应的摄氏温度是: {c:.1f}')