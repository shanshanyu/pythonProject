'''
create_time: 2023/6/2 15:48
author: yss
version: 1.0
'''

#交叉表

import pandas as pd

data = {'name':['tom','tom','jerry','jerry'],'subject':['math','chinese','math','chinese'],'score':[1,2,3,4]}

df = pd.DataFrame(data)
print(df)

cross = pd.crosstab(df['name'],df['subject'])  #创建交叉表，用 name 当索引，subject 当列名
print(cross)