'''操作csv文件'''

import csv
import random


def main():
    with open('csv_test.csv','w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['姓名','语文','数学','英语'])
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        for name in names:
            scores = [random.randrange(50,101) for _ in range(3)]
            scores.insert(0, name)
            writer.writerow(scores)


if __name__ == '__main__':
    main()