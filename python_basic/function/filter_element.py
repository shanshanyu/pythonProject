# 2024/8/4  15:15
items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))  # 把对2取余不等于0的数做一个平方
print(items1)