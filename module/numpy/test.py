'''
create_time: 2023/6/1 15:20
author: yss
version: 1.0
'''

import numpy as np

a = np.array([1,2,3])  #ndarray   [{1:2},{2:3},{3:4}]

a = np.array([[1,2],[3,4]])  #[[1 2]   \n[3 4]] <class 'numpy.ndarray'>


a = np.array([[1,2],[3,4]],ndmin=3,order='C')  #最少三维数组

print(a,type(a))

