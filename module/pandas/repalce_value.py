'''
create_time: 2023/6/2 08:10
author: yss
version: 1.0
'''
import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

df['stuno'] = df['stuno'].replace(to_replace=2,value=15)  #替换某一个单元格的值   也可以指定正则
df['stuno'] = df['stuno'].replace(3,10)  #把 3 替换成 10
print(df)


#将特定值替换为缺失值
df = df.replace(90,70)  #将 90 替换成 70
print(df)
df.replace(91,pd.NaT,inplace=True)  #把 91 替换成 NaN
print(df)

#df.fillna(0,inplace=True)  #将缺失值替换成 0

#df.fillna(method='ffill',inplace=True)  #向前填充

#df.fillna(value={'math':0},inplace=True)  #将math这一列的缺失值填充为 0

#df.dropna(inplace=True)  #删除包含缺失值的行
#df.dropna(axis=1,inplace=True)  #删除包含缺失值的列

new_df = df.dropna(subset=['math'])  #删除 math 列包含缺失值的行
print(new_df)







