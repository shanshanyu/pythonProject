'''
create_time: 2023/6/1 14:51
author: yss
version: 1.0
'''
import prettytable as pt

#data = [['a',1],['b',2]]  # a 1 会是 1 行， b 2 会是一行   只有这种方法能用，列表嵌套列表

#data = {'name':[1,2,3],'age':[2,3,4]}  这种字典格式不适用于 pt

data = [{1 : 2}, {1 : 3}, {1 : 4}]  #会把字典的 key 当做一行  不符合预期

tb = pt.PrettyTable() #参数是 field_names  列名未指定会变成 Field 1，Field 2
tb.add_rows(data)
print(tb)

