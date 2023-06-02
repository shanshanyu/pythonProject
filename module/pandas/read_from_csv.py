'''
create_time: 2023/6/1 16:13
author: yss
version: 1.0
'''

import pandas as pd

tb = pd.read_csv('student.csv')
#print(tb.head())  默认读取前 5 行，可以指定 n
#print(tb.tail())  默认读取后 5 行
#print(tb.info())

print(tb.to_string())