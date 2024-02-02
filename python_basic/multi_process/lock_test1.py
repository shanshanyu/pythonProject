'''
create_time: 2023/6/25 21:27
author: yss
version: 1.0
'''

import fcntl
import time

with open('/tmp/test','w') as f:
    fcntl.flock(f,fcntl.LOCK_EX)
    print('hello')
    time.sleep(100)
