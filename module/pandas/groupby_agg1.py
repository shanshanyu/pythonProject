'''
create_time: 2023/6/2 09:02
author: yss
version: 1.0
'''
import pandas as pd

data = {'name':['tom','tom','jerry','jerry'],'subject':['math','chinese','math','chinese'],'score':[1,2,3,4]}

df = pd.DataFrame(data)
print(df)

#分组  聚合

new_df = df.groupby(['name','subject'])
print(new_df,type(new_df))

new_df = df.groupby(['name','subject']).mean()
print(new_df)

