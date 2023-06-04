'''
create_time: 2023/6/2 15:40
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

print(df.iterrows(),type(df.iterrows()))
print('-'*100)

#遍历 df 对象
for index,row in df.iterrows():  #返回一个元组迭代器   每个元组是一个 index,series
    print(index)
    print(row)
    print(type(index))
    print(type(row))

