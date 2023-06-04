'''
create_time: 2023/6/2 06:42
author: yss
version: 1.0
'''
import pandas as pd

data = {'product':['a','b','c','a','b','c'],'sale-date':['2022-01-01','2022-01-01','2022-01-01','2022-01-02','2022-01-02','2022-01-02'],'money':[1,2,3,4,5,6]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

agg_df = df.groupby('product')['money'].agg(['sum','mean'])   #对分组后的数据进行聚合操作

agg_df = df.groupby('product')  #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fb7a0678668>
agg_df = df.groupby('product')['money'] #<pandas.core.groupby.generic.SeriesGroupBy object at 0x7f8b19039ba8>

agg_df = df.groupby('product')['money'].agg(['sum','mean','count'])   #对分组后的数据进行聚合操作
print(agg_df,type(agg_df))  #agg_df 是一个 DataFrame

agg_df = df.groupby('product')
print(agg_df)

