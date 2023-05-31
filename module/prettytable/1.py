'''
create_time: 2023/5/30 21:45
author: yss
version: 1.0
'''
from prettytable import PrettyTable  #使用程序中产生的数据，如果从数据源中读取数据一般用pandas

tb = PrettyTable(['name','age','country'])  #构造PrettyTable对象的时候也就是初始化了 fieldsname 属性
tb.field_names = ['name1','age','country1']  #覆盖构造函数的 field_names 值
tb.title = 'student info'  #设置表头

#通过列表嵌套列表的方式可以一次性加入多行

tb.add_row(['zhangsan',15,'zhongguo'])
tb.add_row(['lisi',16,'zhongguo'])
tb.add_column('sex',['male','female'])  #列的长度需要和当前行的长度一致


tb.align['name'] = 'l'  #设置对齐样式，默认居中对齐， l   c   r
print(tb)
print(tb.get_string(sortby='age',reversesort=True))
print(tb.get_string())
