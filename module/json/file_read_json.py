'''
create_time: 2023/6/1 16:26
author: yss
version: 1.0
'''

import json
with open('test1.json','r',encoding='utf-8') as file:
    data = file.readlines()  #read读出来的是一个字符串，但是包含了很多行，每行是一个 json 字符串
    for i in data:
        new_data = json.loads(i)  #json loads 一次只能解析一条 json 字符串
        print(new_data,type(new_data))