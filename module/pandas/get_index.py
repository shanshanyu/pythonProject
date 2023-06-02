'''
create_time: 2023/6/1 18:06
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':[10,11,12],'e':['a','b','c']}

df = pd.DataFrame(data)
print(df)
print(df.index,type(df.index))  #RangeIndex 对象  行数
#RangeIndex(start=0, stop=3, step=1)
