'''
create_time: 2023/6/2 15:54
author: yss
version: 1.0
'''
import pandas as pd

data = {'name':['tom','tom','jerry','jerry'],'subject':['math','chinese','math','chinese'],'score':[1,2,3,4]}

df = pd.DataFrame(data)
print(df)

#重塑df，把 name 当做索引，subject 当做 columns，score 当做 value

new_df = df.pivot(index='name',columns='subject',values='score')
print(new_df)

