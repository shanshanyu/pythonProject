'''
create_time: 2023/5/5 17:11
author: yss
version: 1.0
'''


import logging
logging.basicConfig(filename='test.log', filemode='w', level=logging.DEBUG)
logging.debug('debug')
logging.info('info')
logging.warning('warnning')

'''
调用 logging.basicConfig 发生了什么？
修改 root 记录器，设置 fomatter,设置handler
'''
