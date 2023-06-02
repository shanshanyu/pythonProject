'''
create_time: 2023/6/2 08:03
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())


print(df.loc[2,'chinese'],type(df.loc[2,'chinese']))  #获取某一个单元格的值



