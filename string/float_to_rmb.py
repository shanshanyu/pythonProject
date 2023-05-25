'''
create_time: 2023/5/16 14:37
author: yss
version: 1.0
'''

han_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']

unit_list = ['十','百','千']

def fraction_to_han(num):
    if int(num) == 0:
        return ''
    res = ''
    if len(num) == 1:
        res = han_list[int(num[0])] + "分"
    elif len(num) == 2:
        res = han_list[int(num[0])] + "角" + han_list[int(num[1])] + "分"
    return res


#数字字符串换换成中文字符
def four_to_han(num):
    result = ''
    for i in range(len(num)):
        #如果不是最后一个数字并且值不是 0
        if i != len(num)-1 and num[i] !='0':
            result += han_list[int(num[i])] + unit_list[len(num)-i-2]  #len- i 表示在列表中的位置
        else:
            result += han_list[int(num[i])]
    return result


def float_to_rmb():
    try:
        num = float(input("input num: "))
        num = round(num,2)  #num 只保留 2 位小数
        print(num)
        #整数部分
        integer = int(num)
        print(integer)
        #小数部分
        #fraction = int((num - integer)*100)
        fraction = round((num-integer)*100)
        print(fraction)
        integer_len = len(str(integer))
        if integer_len <= 4 :
            res = four_to_han(str(integer)) + "元" + fraction_to_han(str(fraction))
            print(res)
        elif integer_len <= 8 :
            res = four_to_han(str(integer)[:-4]) + "万" + four_to_han(str(integer)[-4 :]) + "元" \
                  + fraction_to_han(str(fraction))
            print(res)
        elif integer_len <= 12 :
            res = four_to_han(str(integer)[:-8]) + "亿" + four_to_han(str(integer)[-8 :-4]) + "万" \
                  + four_to_han(str(integer)[-4 :]) + "元"+fraction_to_han(str(fraction))
            print(res)
        else :
            print("num too long")
    except ValueError as e:
        print(e.__str__())
    except:
        print("unknow exception.")



if __name__ == '__main__':
    float_to_rmb()
