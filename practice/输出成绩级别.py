'''
如果输入的成绩在90分以上（含90分），则输出A；输入的成绩在80分到90分之间（不含90分），则输出B；输入的成绩在70分到80分之间（不含80分），则输出C；输入的成绩在60分到70分之间（不含70分），则输出D；输入的成绩在60分以下，则输出E
'''

score = int(input('请输入成绩: '))

if score >= 90:
    level = 'A'
elif score >= 80:
    level = 'B'
elif score >= 70:
    level = 'C'
elif score >= 60:
    level = 'D'
else:
    level = 'E'

print('您的level是%s' % level)