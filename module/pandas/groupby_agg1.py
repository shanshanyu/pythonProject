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

new_df = df.groupby(['name','subject'])  #分组  DataFrameGroupby 对象
print(new_df,type(new_df))

new_df = df.groupby(['name','subject']).mean()  #分组后取中位数
print(new_df,type(new_df))

new_df = df.groupby(['name']).sum()  #分组后求和
print(new_df,type(new_df))

