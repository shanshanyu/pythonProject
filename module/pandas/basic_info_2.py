'''
create_time: 2023/6/2 07:20
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

new_df = df[1:3]  #通过索引是选择行，通过列名是选择列
print(new_df)

new_df1 = df['math']
print(new_df1)

#获取某个范围内的数据 ！！！！
'''
先去掉原来的索引，用某一列当做索引，然后用 df.loc[:]加切片实现
'''
df.set_index('stuno',inplace=True)  #去掉原来的索引，使用 stuno 当做索引
print(df)

