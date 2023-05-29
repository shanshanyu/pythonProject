'''
create_time: 2023/5/29 17:17
author: yss
version: 1.0
'''

#密码验证，要求 4 位且必须都是数字

import re
prog = re.compile('\d{6}')

def pass_verify():
    password = input('input your password: ')
    if prog.match(password):
        print('支付密码合法')
    else:
        print('支付密码不合法，只能是6位数字')

if __name__ == '__main__':
    pass_verify()
