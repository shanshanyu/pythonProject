'''
create_time: 2023/5/16 11:36
author: yss
version: 1.0
'''

import json

d = {'a':1,'b':2}

with open('test.txt','a',encoding='utf-8') as f:
    json.dump({'张三':2,'c':3},f,ensure_ascii=False)
    f.write('\n')

#print(json.dump(d))

print(json.dumps(d))  #把python对象转换成 json 字符串
print(type(json.dumps(d)))

