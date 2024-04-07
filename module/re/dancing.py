'''
create_time: 2024/4/7 15:49
author: yss
version: 1.0

匹配I love dancing and reading中的第一个 ing

\b：匹配单词的边界
\B：匹配非单词的边界


(?=...) 和 ... 匹配了再匹配前面的字符

(?<=...) 和 ... 匹配了再匹配后面的字符

'''
import re


def main():
    str1 = '匹配I love dancing and reading中的第一个 ing'
    res = re.search(r'(?<=\bdanc)\w+\b',str1)
    print(res)

    res1 = re.search(r'\b\w+(?=ing)',str1)
    print(res1)

if __name__ == '__main__':
    main()

