'''
create_time: 2023/6/1 18:02
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':[10,11,12]}
df = pd.DataFrame(data)

print(df.columns,type(df.columns))
for i in df.columns:
    print(i)