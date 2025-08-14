'''国内运营商号码段'''

import re


def verify_phone(sentence):
    # 创建正则表达式对象，使用前瞻和回顾来保证前后没有数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}\s*')
    result = re.findall(pattern, sentence)  # 返回值是列表
    #没有捕获组或者只有一个捕获组，返回值是列表，如果有多个组，返回值是列表嵌套元组

    for tel in result:
        print(tel)
    print('-'*100)

    # 通过迭代器取出匹配对象
    for tel in re.finditer(pattern, sentence):  # 返回值是match 对象的迭代器
        print(tel.group())   #m.group() 只有一个参数，结果是字符串。参数为0，表示返回整个匹配字符串
    print('-'*100)


    #通过search函数找出所有匹配
    m1 = pattern.search(sentence)  #返回第一个匹配的match对象
    while m1:
        print(m1.group())
        m1 = pattern.search(sentence,m1.end(0))


def main():
    sentence = '重要的事情说3遍，我的号码是：15375456189a'
    verify_phone(sentence)


if __name__ == '__main__':
    main()



