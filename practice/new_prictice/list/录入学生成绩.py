names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩

scores = [[None]*len(courses) for _ in range(len(names))]
for i,name in enumerate(names):
    for j,course in enumerate(courses):
        scores[i][j]= int(input(f'请输入{name} {course} 成绩：'))

print(scores)




