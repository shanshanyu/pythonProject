# 2024/8/4  10:56
# 嵌套列表
# 生成一个二维数组

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩


#scores = [[None]*len(courses)]*len(names)  # 外部列表的子列表都是同一个对象
scores = [[None]*len(courses) for _ in range(len(names))]
i = 0
for name in names:
    j = 0
    for course in courses:
        score = int(input(f'请输入{name}的{course}成绩:'))
        scores[i][j] = score
        j += 1
    i += 1
    print(scores)
print(scores)



