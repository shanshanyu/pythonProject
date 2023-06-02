'''
create_time: 2023/6/2 07:40
author: yss
version: 1.0
'''
#计算某一列的总和
#学过了分组 和 聚合  groupby   agg

import pandas as pd

data = {'stuno':[1,2,3],'math':[90,91,92],'chinese':[80,81,82]}

df = pd.DataFrame(data)
print(df.to_string())

print(df['math'],type(df['math']))  #df['math] 是一个 <class 'pandas.core.series.Series'>

new_df = df['math'].sum()  #获取某一列的和 ！！！！
print(new_df,type(new_df))  #numpy.int64  对象

new_df1 = df['math'].mean()    #获取某一列的平均值
print(new_df1,type(new_df1))

print('-'*100)
new_df2 = df['math'].median()  #计算中位数
print(new_df2,type(new_df2))

new_df3 = df['math'].std()  #计算某一列的标准差
print(new_df3,type(new_df3))

new_df4 = df['math'].var()  #计算某一列的方差
print(new_df4,type(new_df4))

new_df5 = df['math'].max()  #获取某一列的最大值
print(new_df5,type(new_df5))

new_df6 = df['math'].min()   #获取某一列的最小值
print(new_df6,type(new_df6))

print('-'*100)
print(df)
#修改列名
df.rename(columns={'stuno':'编号'},inplace=True)
df.set_index('编号',inplace=True)
print(df)




