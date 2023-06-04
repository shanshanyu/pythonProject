'''
create_time: 2023/6/2 15:35
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':['10','11',12]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)
print(df.dtypes)

#把 d 列从 object 转换成 int64

df['d'] = df['d'].astype(int)
print(df.dtypes)