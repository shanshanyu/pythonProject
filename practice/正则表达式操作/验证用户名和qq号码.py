'''要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0'''
import re


def verify_username(username):
    m1 = re.match(r'^\w{6,20}$',username)
    if not m1:
        return -1
    return 0


def verify_qq(qq):
    m1 = re.fullmatch(r'[1-9]\d{4,11}',qq)
    if not m1:
        return -1
    return 0


def main():
    username = input('请输入用户名：')
    qq = input('请输入qq号：')

    if verify_username(username):
        print('用户名不合法')
        return -1
    if verify_qq(qq):
        print('qq输入有误')
        return -1
    print('验证通过！')

if __name__ == '__main__':
    main()

