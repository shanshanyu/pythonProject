'''
create_time: 2023/6/1 22:55
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[11,5,6],'C':[7,8,9],'d':[10,11,12]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

new_df = df.sort_values(by='B')  #根据列进行排序，不会改变原来的 DataFrame  升序
print(new_df)

new_df = df.sort_values('B',ascending=False)
print(new_df)

