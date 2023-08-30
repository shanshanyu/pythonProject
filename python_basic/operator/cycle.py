'''
create_time: 2023/8/30 17:12
author: yss
version: 1.0
根据半径计算周长和面积
'''

import math
r = float(input('请输入半径：'))

perimeter = 3.1415926 * 2 * r

area = 3.1415926 * pow(r,2)

print(f'周长是 {perimeter:.2f}')
print(f'面积是{area:.2f}')
