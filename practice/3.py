'''
create_time: 2023/5/29 16:09
author: yss
version: 1.0
'''
#进制转换
#bin 转换成二进制数字，oct 转换成八进制数字，hex转换成十六进制数字,结果都是字符串


x = int('101',2)  #如果base存在，x 必须是字符串
print(x)

x = int(0x101)  #int 把其他进制的数字转换成 10 进制数字，或者把浮点数转换成整型10进制数
print(x)

print(bin(10),type(bin(10)))  #bin  oct  hex 返回值是 str
print(bin(0x101)) #bin转换成二进制，输入一个整型数，可以是  2   8  16 10 进制的数

'''
bin   oct   hex   int
bin转换成二进制，输入一个整型数，可以是 2  8  16 10 进制的数字，输出是一个字符串
oct转换成八进制，输入一个整型数，可以是 2  8  16 10 进制的数字，输出是一个字符串
hex转换成十六进制，输入一个整型数，可以是 2  8  16 10 进制的数字，输出是一个字符串
int转换成十进制的整数，输入可以是字符串或者是 2 8 16 10 进制的数字，输出是一个整数
'''


#进制转换
def display_numer(num):
    print(f'{num}的二进制数字为：{bin(num)}')
    print('%d的二进制数字为：%s' % (num,bin(num)))  #格式化字符串，用 %   用 format 也可以
    print('{}的二进制数字为: {}'.format(num, bin(num)))
    print(f'{num}的八进制数字为：' + oct(num))
    print(f'{num}的十六进制数字为：' + hex(num))

if __name__ == '__main__':
    try:
        num = int(input('请输入一个十进制的整数：'))
        print(num,type(num))
    except:
        print('输入无效，不是一个数字')

    display_numer(num)