'''
create_time: 2023/5/29 20:29
author: yss
version: 1.0
'''

#模拟用户登录，3次输入错误退出

for i in range(3):
    username = input('请输出用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == '8888':
        print('登录成功')
        break
    else:
        print('用户名或密码不正确')
        if i < 2:
            print(f'您还有{2-i}次机会')
        else:
            print('三次均输入错误，程序退出')