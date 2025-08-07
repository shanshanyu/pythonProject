'''设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置'''
import string
import random


def generate_code(num):
    ASCII_CHAR = string.ascii_letters + string.digits
    code = ''
    for _ in range(num):
        code += random.choice(ASCII_CHAR)
    return code


def generate_code_1(num):
    ASCII_CHAR = string.ascii_letters + string.digits
    return ''.join(random.choices(ASCII_CHAR, k=num))


if __name__ == '__main__':
    ret = generate_code_1(5)
    print(ret)



