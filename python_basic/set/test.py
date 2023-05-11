'''
create_time: 2023/4/26 09:43
author: yss
version: 1.0
'''

#打印set集合的所有方法

a = [e for e in dir(set) if not e.startswith('__')]
print(a)