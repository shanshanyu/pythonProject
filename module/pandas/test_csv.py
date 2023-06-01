'''
create_time: 2023/6/1 15:35
author: yss
version: 1.0
'''

import pandas as pd   #文件名不能用 csv，会冲突
print(pd.__version__)  #pandas 版本 1.1.5
#tb = pd.DataFrame({'name':[1,2,3],'age':[4,5,6]})
#print(tb)
name = ['zhangsan','lisi','wangwu']
age = [15,16,17]

d = {'name':name,'age':age}
tb = pd.DataFrame(d)

#tb = pd.Series([1,2,3])
print(tb)

tb.to_csv('student.csv')
