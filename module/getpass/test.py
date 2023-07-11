'''
create_time: 2023/7/10 17:13
author: yss
version: 1.0
'''

import getpass

a = getpass.getpass('input your pass: ')  #获取密码
print(a)


b = getpass.getuser()  #获取用户名
print(b)
