# 2023/7/10 21:35

a = '''
a1
b2
c3
d4
'''

print(a)

for i in a:  #遍历字符串，打印一个个字符
    print(i)

b = a.split('\n')  #通过换行对字符串进行分割
print(type(b),b)  #分割后是一个列表