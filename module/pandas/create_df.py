'''
create_time: 2023/6/1 16:33
author: yss
version: 1.0
'''
import pandas as pd

lst = [('zhangsan',15),('lisi',20)]  #列表嵌套元组，列表也可以嵌套列表

df = pd.DataFrame(lst)
print(df)