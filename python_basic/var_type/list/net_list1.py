# 2024/8/4  14:45
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩

scores = [[None]*len(courses) for _ in range(len(names))]
i = 0
for i,name in enumerate(names):
    for j,course in enumerate(courses):
        score = int(input(f'请输入{name}的{course}成绩:'))
        scores[i][j] = score

print(scores)