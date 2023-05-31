'''
create_time: 2023/5/30 20:27
author: yss
version: 1.0
'''

#输入成绩

def input_score():
    score = int(input('输入学生成绩：'))
    assert  0 <= score <= 100
    print(score)

if __name__ == '__main__':
    input_score()