'''
create_time: 2023/6/2 20:04
author: yss
version: 1.0
'''
import pandas as pd

data = {'product':['a','b','c','a','b','c'],'sale-date':['2022-01-01','2022-01-01','2022-01-01','2022-01-02','2022-01-02','2022-01-02'],'money':[1,2,3,4,5,6]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

new_df = df.groupby('product')  #只显示一列 product   按一列进行分组
#new_df = df.groupby(['product','sale-date'])
print(new_df)
print(new_df.sum('money'))  #分组聚合