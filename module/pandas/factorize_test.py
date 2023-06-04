'''
create_time: 2023/6/2 16:00
author: yss
version: 1.0
'''
import pandas as pd

data = {'name':['tom','tom','jerry','jerry'],'subject':['math','chinese','math','chinese'],'score':[1,2,3,4]}

df = pd.DataFrame(data)
print(df)

factorized,_ = pd.factorize(df['score'])
df['new_score']  = factorized
print(df)