# 2024/1/18 21:02
# input 获取多个输入，然后 map 成整数

'''
  input只能得到一个字符串，要想得到多个数值，需要调用 split 方法，然后 map 对序列做映射，把 str 转换成 int

'''
# try:
#     a,b = map(int,input('请输入两个整数，以空格分隔').split())
#     print(a + b)
# except Exception as e:
#     print('有异常了')
#
#
# tencent = input()
# ali = input()
#
# if tencent > ali:
#     print('tencent')
# else:
#     print('ali')

# choice = 'vscode' if int(input()) == 0 else 'pycharm'
# print(choice)

# a,b,c = map(int,input().split())
#
# if max(a,b,c) == a:
#     print('python')
# elif max(a,b,c) == b:
#     print('java')
# elif max(a,b,c) == c:
#     print('c')


def test(h:int):
    return 2*h

class Test:
    a = 3.4
    print(test(a))