'''
create_time: 2023/5/16 11:32
author: yss
version: 1.0
'''

import sys
print(sys.argv)  #列表

try:
    sys.exit("abnormal")  #sys.exit 是产生一个 SystemExit 异常，为什么没有被Exception捕获到
    #systemexit不是exception的子类
except SystemExit:
    print('error occur')
finally:
    print('over')



print(sys.path) #path路径

print(sys.platform)  #平台


print(sys.version)