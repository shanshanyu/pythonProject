'''
create_time: 2023/6/1 17:19
author: yss
version: 1.0
'''

#向数据库中插入数据，功能暂未实现

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import  *

df = pd.DataFrame({'name':[1,2,3],'age':[2,3,4]})

engine = create_engine('mysql+mysqlconnector://root:"iflytek@123"@123.56.222.255:3306/student')

df.to_sql('t2',engine)