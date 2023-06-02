'''
create_time: 2023/6/2 06:55
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

data1 = {'stuno':[1,2,3],'english':[99,98,97]}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)


print(df)
print(df1)

new_df = pd.merge(df,df1,on='stuno')  #将两个表格按照指定列进行合并  类似于 sql 中的 join
print(new_df)
print('-'*100)
new_df1 = pd.concat([df,df1])  #合并表格，会有很多 NaN
print(new_df1)
