'''
条件运算符的嵌套
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

def level():
    score = int(input('input your score: '))
    if score >= 90:
        print('A')
    if score >= 60:
        print('B')
    else:
        print('C')

def main():
    level()


if __name__ == '__main__':
    main()


