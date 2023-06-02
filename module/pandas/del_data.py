'''
create_time: 2023/6/2 07:03
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

new_df = df.drop('chinese',axis=1,inplace=True)  #会修改原来的 df   axis=1 表示跨列，axis=0 表示跨行
#drop 有一个 inplace 参数，如果设置为 True，表示会修改原来的df，如果设置为 False，返回一个新的 df

print(df)
print(new_df)

df.drop(1,inplace=True)   #通过 drop 方法删除一行  axis 默认为 0，操作行，通过索引
print(df)


