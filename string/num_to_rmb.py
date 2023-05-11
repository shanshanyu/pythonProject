'''
create_time: 2023/5/4 14:42
author: yss
version: 1.0
'''

num_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
unit_list = ['十','百','千']


def four_to_str(substr):
    '''四位数字字符串转换成四位中文字符串'''
    result = ''
    num_len = len(substr)
    for i in range(num_len):
        if i != (num_len-1) and substr[i] != '0':
            #逻辑在这里
            result += num_list[int(substr[i])] + unit_list[num_len-i-2]
        else:
            result += num_list[int(substr[i])]
    return result



def num_to_rmb(num):
    integer = int(num)
    fraction = round((num-integer)*100)
    if len(str(integer)) > 12:
        print("num too long")
        return
    elif len(str(integer)) > 8:   #亿级别
        return four_to_str(str(integer)[:-8]) +"亿" + four_to_str(str(integer)[-8:-4]) +"万"+ four_to_str(str(integer)[-4:])+"元"
    elif len(str(integer)) > 4:  #万级别
        return four_to_str(str(integer)[:-4]) +"万"+ four_to_str(str(integer)[-4:])+"元"
    else:
        return four_to_str(str(integer)[-4:])+"元"


if __name__ == '__main__':
    print(num_to_rmb(412345))