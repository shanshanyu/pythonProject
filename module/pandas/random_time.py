'''
create_time: 2023/6/2 16:07
author: yss
version: 1.0
'''
import pandas as pd
import numpy as np

start_time = '2023-01-01'
end_time = '2023-05-01'

date_range = pd.date_range(start=start_time,end=end_time)  #返回 DatatimeIndex 对象，可迭代对象
print(date_range,type(date_range))

print(np.random.choice(date_range,size=10),type(np.random.choice(date_range,size=10)))  #ndarray

sample_date = pd.Series(np.random.choice(date_range,size=10))  #从 DatetimeIndex中取 10 个
print(sample_date,type(sample_date))