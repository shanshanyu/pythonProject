'''
create_time: 2023/5/10 16:45
author: yss
version: 1.0
'''

import yaml

with open('test.yml','r',encoding='utf-8') as f:
    file_data = f.read()
    print(file_data)
    print(type(file_data))

    data = yaml.load(file_data,yaml.FullLoader)
    print(data)
    print(type(data))