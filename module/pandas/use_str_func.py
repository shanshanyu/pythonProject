'''
create_time: 2023/6/2 16:21
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':['a,b','11,10','15,12']}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

df['d']  = df['d'].str.strip()  #把 d 列转换成字符串，然后去掉每个单元格的左右空白   strip  replace  lower  upper
print(df)

#df['d1','d2'] = df['d'].str.split(',')    #如果不加 expand 会拆分成一个列表，列名是元组,增加的是一列

df[['d1','d2']] = df['d'].str.split(',',expand=True)  #增加两列，
print(df)