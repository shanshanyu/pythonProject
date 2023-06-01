'''
create_time: 2023/6/1 09:25
author: yss
version: 1.0
'''

#Series 相当于一列

#data=None, index=None, dtype=None, name=None
import pandas as pd
a = [1,2,3]  #生成一列 1 2 3，没有列名
b = {'a':1,'b':2,'c':3}
#tb = pd.Series(a,index =['a','b','3'],name='tb test')  #index的长度需要和 data 的长度一致

tb = pd.Series(b,index=['a','b'])  #如果data 是字典，index 等于是字典的 key，长度可以和字典不一致
tb = pd.Series(b)  #生成一列 1 2 3，列名没有，索引名 'a','b','c'
#tb = pd.Series(a)
print(tb)

