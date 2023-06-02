'''
create_time: 2023/6/2 07:28
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

#获取数学成绩大于 90 的行
bool_index = df['math'] > 90
print(bool_index,type(bool_index))

new_df = df[bool_index]
print(new_df)
print(df)

print(df[['stuno','chinese']])  #读取两列

print(df[1:2])  #读取一行  如果只传递 1 会报错，因为会去找列名等于 1 的列
print(df.loc[0])

