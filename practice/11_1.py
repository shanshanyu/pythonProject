'''
create_time: 2023/5/30 20:41
author: yss
version: 1.0
'''

#输入 3 个参数，判断能否构成三角形

import math
def test_trigger():
    try:
        trigger_lst = []
        num1 = int(input('请输入第一条边：'))
        num2 = int(input('请输入第二条边：'))
        num3 = int(input('请输入第三条边：'))
        if num1 < 0 or num2 < 0 or num3 < 0:
            raise Exception('三条边不能为负数')
        trigger_lst.append(num1)
        trigger_lst.append(num2)
        trigger_lst.append(num3)
        trigger_lst.sort()

    except Exception as e:
        print(e)
        return

    if math.pow(trigger_lst[0],2) + math.pow(trigger_lst[1],2) == math.pow(trigger_lst[2],2):
        print('可以构成三角形')
    else:
        print('不能构成三角形')

if __name__ == '__main__':
    test_trigger()