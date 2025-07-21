'''
输入一个圆的半径r，计算出它的周长（ 2πr）和面积（ πr2）
'''
import math

r = float(input('请输入半径： '))

circle = 2 * math.pi * r

area = math.pi * r * r

print('周长=%.1f，面积=%.1f' % (circle, area))