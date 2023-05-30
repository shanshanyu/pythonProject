'''
create_time: 2023/5/30 12:03
author: yss
version: 1.0
'''

#对 test.sjon 里面的 json 数据进行去重排序
a = {}
b = {'a'}  #花括号里面放一个元素才会被当做集合
print(type(a))  #使用花括号默认创建的是字典，
print(type(b))
print('-'*50)

import json
distinct_set = set()

def sort_time(d):
    return json.loads(d)['time']

#去重
with open('test.json','r',encoding='utf-8') as file:
    file_data = file.readlines()  #一行一条 json 数据，读出来的 json 数据放到列表中
    for i in file_data:   #i 是一个 json 字符串
        distinct_set.add(i)

tmp_list = []
#去重后放入列表进行排序
with open('result.json','w',encoding='utf-8') as r_file:
    #去重后的数据放入列表
    for i in distinct_set:
        tmp_list.append(i.strip())
    #列表排序
    tmp_list.sort(key=sort_time)
    for i in tmp_list:
        r_file.write(i+'\n')



