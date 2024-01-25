# 2024/1/24 21:00
'''
从键盘获取 4 位数字，分别输出个、十、百、千位上的数字
还可以通过字符串的索引来处理
'''

num = int(input('input num: '))
thousand = num//1000
hundred = num//100%10
ten = num//10%10
one = num%10

print(thousand,hundred,ten,one)
