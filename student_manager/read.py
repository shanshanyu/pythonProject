# 2023/5/28  20:22
with open('stu_info.txt','r',encoding='utf-8') as file:
    data = file.read()
    print(data,type(data))

#read会读取文件中的所有字符，返回值是一个字符串
#readlines会读取文件中的所有行，每行结尾一个'\n'换行符。返回值是一个列表

#write会向文件中输出一个字符串
#writelines会向文件中输出一个可迭代对象，可以是字符串，可以是列表


