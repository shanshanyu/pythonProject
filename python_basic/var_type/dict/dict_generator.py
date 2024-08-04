# 2024/8/4  9:58
# 字典生成式，筛选字典中的一部分 kv 组成一个新字典
'''
用股票价格大于100元的股票构造一个新的字典
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

new_prices = {k:v for k,v in prices.items() if v > 100}
print(new_prices)

a = None
print(type(a))