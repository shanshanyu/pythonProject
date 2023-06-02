'''
create_time: 2023/6/1 23:02
author: yss
version: 1.0
'''
import pandas as pd

data = {'product':['a','b','c','a','b','c'],'sale-date':['2022-01-01','2022-01-01','2022-01-01','2022-01-02','2022-01-02','2022-01-02'],'money':[1,2,3,4,5,6]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

#生成透视表   以product 为索引，日期为
new_df = df.pivot_table(index='product',columns='sale-date',aggfunc='sum',values='money')
print(new_df)