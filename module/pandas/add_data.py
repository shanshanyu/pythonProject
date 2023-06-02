'''
create_time: 2023/6/2 07:13
author: yss
version: 1.0
'''

import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

new_row = {'stuno':4,'math':89,'chinese':90}
df.loc[len(df)] = new_row  #通过 loc 添加一行  会在原来的表格中进行修改
print(df)



