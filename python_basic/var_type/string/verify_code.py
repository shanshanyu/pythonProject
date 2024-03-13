'''
create_time: 2024/3/7 11:17
author: yss
desc: 生成指定长度的验证码
version: 1.0

创建一个字符串(里面包含大小写字符和数字）-> 根据输入的长度，执行多少次循环取出字符到目标字符串中->打印目标字符串
'''
import random

def get_verify_code(n=4):
    res = ''
    model = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678'
    # for i in range(n):
    #     res += random.choice(model)
    #是否也可以通过 choices 方法实现？
    res = res.join(random.choices(model,k=n))   #字符串的 join 方法可以把一个序列元素的字符串表示转换成字符串
    #split()分割字符串，默认以 " " 为分隔符

    return res




def main():
    res = get_verify_code()
    print(res)

if __name__ == '__main__':
    main()
