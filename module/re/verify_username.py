'''
create_time: 2024/4/7 14:15
author: yss
version: 1.0

验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
'''

import re

def verify_username(username):
    prog = re.compile(r'^\w{6,20}$')
    return prog.match(username)


def verify_qq(qq):
    prog = re.compile(r'^[1-9]\d{4,11}$')
    return prog.match(qq)


def main():
    username = input('input username: ')
    if verify_username(username):
        print('username valid')
    else:
        print('username invalid')

    qq = input('input qq number: ')
    if verify_qq(qq):
        print('qq valid')
    else:
        print('qq invalid')

if __name__ == '__main__':
    main()