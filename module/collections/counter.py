'''
create_time: 2024/6/13 18:06
author: yss
version: 1.0
desc: collections 模块 counter 类  键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。
'''


from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

counter = Counter(words)
print(counter.most_common(3))   # 结果： [('eyes', 8), ('the', 5), ('look', 4)]

