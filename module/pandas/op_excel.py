'''
create_time: 2023/6/2 21:06
author: yss
version: 1.0
'''

import pandas as pd

data = {'product':['a','b','c','a','b','c'],'sale-date':['2022-01-01','2022-01-01','2022-01-01','2022-01-02','2022-01-02','2022-01-02'],'money':[1,2,3,4,5,6]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

df.to_excel('test1.xlsx',index=False)
