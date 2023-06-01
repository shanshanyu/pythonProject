'''
create_time: 2023/6/1 09:53
author: yss
version: 1.0
'''

import pandas as pd
#pandas 的 DataFrame 参数可以是列表嵌套列表，字典，列表嵌套字典
#data = [['a',1],['b',2]]  #数据是列表嵌套，如果不指定 columens，默认为 0 1 ..

data = {'name':[1,2,3],'age':[2,3,4]}  #字典的 key 当做列名，

#data = [{1:2},{1:3},{1:4}]  #字典的 key 当做列名

#tb = pd.DataFrame(data,columns=['name','age'])  #创建一个表格
tb = pd.DataFrame(data)   #a  1 是一行，b 2 是一行，列名没有，默认为 0  1
print(tb)

print(tb.loc[0])  #返回第一行的数据   默认 key 为0

print(tb.loc[[0,1]])  #返回第 1  2  两行的数据

tb.index = ['day1','day2','day3']  #创建 DataFrame对象的时候可以指定 index，是一个对象属性，长度必须和行长度一致
print(tb)
print(tb.loc['day1'])   #这里只能指定 day1  day2 或 day3 不能指定其他值


print(tb['name'])  #获取第一列的数据

tb['sum'] = tb['name'] + tb['age']  #新加一列   tb['x'] 获取一列，tb.local['x'] 获取一行
print(tb)

