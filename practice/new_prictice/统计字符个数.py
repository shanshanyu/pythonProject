'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
'''

def count_str():
    input_str = input('输入字符串: ')
    alpha_num = 0
    space_num = 0
    other_num = 0
    for i in input_str:
        if i.isalpha():
            alpha_num += 1
        elif i.isspace():
            space_num += 1
        else:
            other_num += 1
    return alpha_num, space_num, other_num


if __name__ == '__main__':
    ret =  count_str()
    print(ret)