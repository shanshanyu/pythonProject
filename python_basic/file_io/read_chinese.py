# 2023/5/24 21:29

f = open('test.txt', 'rb')  #打开文件需要指定编码，如果不指定编码可以使用二进制模式打开文件
content = f.read()
print(content.decode())
f.close()

f1 = open('test.txt', 'r', encoding='utf-8')
content = f1.read()
print(content)
f1.close()

f2 = open('test.txt', 'r')    #二进制文件采用 b 模式，readline  readlines  writeline  writelines 一般适用文本文件
data = f2.readline()
print(data,type(data))