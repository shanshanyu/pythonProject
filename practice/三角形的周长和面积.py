'''
输入三条边的长度，如果能构成三角形就计算周长和面积；否则给出“不能构成三角形”的提示
'''

a = int(input('请输入第1条边的长度：'))
b = int(input('请输入第2条边的长度：'))
c = int(input('请输入第3条边的长度：'))

if a+b > c and a+c >b and b+c >a:
    print('周长:%.1f' % (a+b+c))
    s = (a+b+c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('面积:%.1f' % area)
else:
    print('不能构成三角形')

