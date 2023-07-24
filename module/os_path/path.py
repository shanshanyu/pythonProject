'''
create_time: 2023/5/10 16:19
author: yss
version: 1.0
os.path.dirname(path)是用split()切分path，然后返回第一部分，split()会把一个path切分成两部分，head和tail，如果路径中没有/，head为空，如果结尾是/，tail为空。
'''

import os.path

print(os.path.abspath('path.py'))
print(os.path.dirname('path.py'))  #返回空