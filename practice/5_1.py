'''
create_time: 2023/5/29 20:14
author: yss
version: 1.0
'''

#模拟密码登录,三次失败退出

count = 0
while count < 3:
    username = input('请输出用户名：')
    password = input('请输入密码：')
    if username != 'admin' or password != '8888':
        print('用户名或密码不正确！')
        count += 1
        if count < 3:
            print(f'您还有{3- count}次机会')
        else:
            print('对不起，三次均输入错误！')
    else:
        print('登录成功')
        break





