'''
create_time: 2023/5/29 19:47
author: yss
version: 1.0
'''
#输出 26 个字母对应的 ascii 码值?   如何遍历 a-z ?    如何把一个字符转变成 ascii 码
#目前没找到遍历方法， ord('a')+i  再用 chr 转换成字符

x = 'a'
for i in range(26):
    print(f'{chr(ord(x)+i)}对应的ascii码是：{ord(x)+i}')  #格式化字符串

x = 97
for i in range(26):
    print(chr(x),'--->',x)
    x = x+1

print(i)  #i是全局变量
