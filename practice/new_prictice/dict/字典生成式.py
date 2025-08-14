

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}


#用大于100的构成一个新字典

new_prices = {k:v for k,v in prices.items() if v > 100}   #字典生成式生成一个新字典
print(new_prices)