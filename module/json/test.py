'''
create_time: 2023/5/12 11:59
author: yss
version: 1.0
'''

import json

res = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  #会把列表转换成 json 中的数据
print(res)

print(json.dumps('abc'))  #会把 str 转换成 json 中的 str
print(json.dumps(1))  #会把 int 类型转换成 json 中的 number


d = dict(a=3,b=4,c=5)
print(d)
print(json.dumps(d)) #把字典转换中 json 中的对象

f = open('test.txt','r',encoding='utf-8')

print(type(json.load(f)))

#json.load   json字符串转换成 python 对象

