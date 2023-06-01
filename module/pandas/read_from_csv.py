'''
create_time: 2023/6/1 16:13
author: yss
version: 1.0
'''

import pandas as pd

tb = pd.read_csv('student.csv')
print(tb.head())
print(tb.tail())
print(tb.info())