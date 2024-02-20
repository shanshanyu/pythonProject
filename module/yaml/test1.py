'''
create_time: 2024/2/18 16:51
author: yss
version: 1.0
'''
import yaml

with open('test1.yaml','r') as f:
    data = yaml.load(f.read(),Loader=yaml.FullLoader)
    print(type(data),data)
