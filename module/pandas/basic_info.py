'''
create_time: 2023/6/1 21:14
author: yss
version: 1.0
'''
import pandas as pd

data = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'d':[10,11,12]}  #3 行 4 列

df = pd.DataFrame(data)

print(df)
print(df.dtypes)  #表格列的类型
print(df.columns)  #表格列名
print(df.shape)  #表格有几行几列  返回值是一个列表
print(df.describe())  #查看统计信息
print(df.head(1))  #显示第一行
print(df.tail(1)) #显示最后一行
print(df.info())  #显示数据的信息
print(df.index)   #显示索引  也就是行数

print('-'*100)
print(df['A'])  #选择某一列


print('-'*100)
print(df.loc[0])  #获取第 1 行的数据
print(df.loc[[0,1]])  #传递一个列表，获取第一行和第二行
print(df.loc[[0,1],['A','d']])  #传递 2 个列表，获取第一行和第二行 A 列的数据
print(df.loc[0,'A'])  #获取第一行，列名为 A 的那一个单元格的数据

#df.index = ['a','b','c']
print('-'*100)
print(df['A'])  #获取一列数据
print(df[['A','B']])  #获取 A B 两列数据

print('-'*100)

print(df.iloc[0,0])  #通过索引获取数据，行和列都是索引
print(df.iloc[0])  #获取第一行的数据，和 df.loc[0] 没有区别

print(df.iloc[:,0])  #获取第 1 列的数据
print('-'*100)
print(df.iloc[:,0:3])  #切片

print(df.iloc[[0,1]])  #获取第 1 2 行
print(df.iloc[[0,1],[0]])  #获取第 1 2 行，第一列的数据

print('-' *100)
#loc 要求列是名字，iloc 要求列是索引

print(df.iloc[:,-1:])  #获取最后一列
print('-'*100)
print(df[['A','B']])  #获取 A B 两列数据
print(df.loc[[0,1]])  #传递一个列表，获取第一行和第二行


#loc   iloc   传递一个参数，获取某一行   传递 2 个参数，获取某行某列   loc 列是列名，iloc 列是索引
#             传递一个列表获取多个列，传递两个列表，获取多行多列的数据

#[] 传一个参数，获取某一列，传一个列表，获取多个列




