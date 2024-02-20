'''
create_time: 2024/2/18 17:03
author: yss
version: 1.0
'''

import yaml

with open('test2.yaml','r') as f:
    data = yaml.load(f.read(),Loader=yaml.FullLoader)
    print(data,type(data))