'''
create_time: 2023/6/1 17:57
author: yss
version: 1.0
'''

#显示行数和列数

import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':[10,11,12]}  #3行4列

df = pd.DataFrame(data)
print(df)
print(df.shape,type(df.shape))  #显示 df 的行和列数  返回值是一个元组

