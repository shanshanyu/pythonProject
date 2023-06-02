'''
create_time: 2023/6/1 22:19
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':[10,11,12]}  #3 行 4 列

df = pd.DataFrame(data)
print(df)

bool_index = df['d'] > 10  #bool_index 是 series 对象
print(bool_index,type(bool_index))

filter = df[bool_index]
print(filter,type(filter))

b = [True,False,False]
b1 = pd.Series(b)
print(b1)

print(df[b1])  #可以直接传递一个Series 对象，Series 对象是 True 或 False然后传入 df 对象，获取某些行

bool_index = df['d'] > 10
print(type(bool_index))  #Series对象  相当于 loc 中的一个列表对象
print(df[bool_index])

#df = df.loc[df['成绩'] >= 90, ['姓名', '成绩']]

print(df.loc[df['d']>10,['A','B']])  #获取 d 列大于 10 的行，列只取 'A' 'B' 两列

print(df.loc[df['A']==2,['C','B']])
