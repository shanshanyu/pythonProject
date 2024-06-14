'''
create_time: 2024/5/24 11:37
author: yss
version: 1.0

desc：# 用股票价格大于100元的股票构造一个新的字典

字典生成式的用法
 生成式（推导式）可以用来生成列表、集合和字典。
'''

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 遍历字典的key，如果 k 对应的 v 大于 100，则写入字典
new_dict = {k:prices[k] for k in prices.keys() if prices[k] > 100}

# 更清晰一点
new_dict1 = {k:v for k,v in prices.items() if v > 100}

print(new_dict)
print(new_dict1)