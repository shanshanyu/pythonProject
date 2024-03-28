'''
create_time: 2024/3/28 11:20
author: yss
version: 1.0

把一个字典写入到文件中:
把字典转换成json字符串->写入文件

desc:
会使用到 json 模块:
json.dump(obj,fp..) 会把 python 对象转换成一个 fp
json.dumps(obj..) 会把 python 对象转换成一个 str

json.load 会把一个 fp 对象序列换成 python 对象
json.loads 会把一个 json 字符串序列换成 python 对象
'''

import json

def main():
    #python字典对象
    j = {
    "name": "骆昊",
    "age": 38,
    "qq": 957658,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320}
    ]
}

    try:
        json_str = json.dumps(j)
        with open('json_file.txt','w',encoding='utf-8') as f:
            f.write(json_str)
    except Exception as e:
        print(e)

    #把数据读出来转换成字符串
    with open('json_file.txt','r',encoding='utf-8') as f1:
        data = json.load(f1)
        print(data,type(data)) #应该是一个 python 字典对象

if __name__ == '__main__':
    main()
