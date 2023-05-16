'''
create_time: 2023/5/16 11:36
author: yss
version: 1.0
'''

import json

d = {'a':1,'b':2}

with open('test.txt','a') as f:
    print(json.dump({'b':2,'c':3},f))

#print(json.dump(d))

print(json.dumps())