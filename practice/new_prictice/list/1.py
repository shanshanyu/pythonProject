'''
create_time: 2024/5/24 11:48
author: yss
version: 1.0

desc: # 录入五个学生三门课程的成绩
'''

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']


scores = [[None]*len(courses) for _ in range(len(names))]
for i in range(len(names)):
    for j in range(len(courses)):
        score = float(input(f'请输入{names[i]}的{courses[j]}成绩：'))
        scores[i][j] = score

print(scores)