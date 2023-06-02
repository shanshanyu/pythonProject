'''
create_time: 2023/6/1 18:13
author: yss
version: 1.0
'''

#获取某一列的数据类型

import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':[2,1,'a']}  #列中的数据类型可以不相同，看 'd' 列

df = pd.DataFrame(data)
print(df)
print(df.dtypes)  # d 列中有 str，d 列的类型是 object

'''
A    int64
B    int64
C    int64
d    object
dtype: object
'''



