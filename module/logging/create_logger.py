'''
create_time: 2023/3/29 09:58
author: yss
version: 1.0
'''

'''
logging 是一个包，包下面有 handlers  模块，config 模块

记录器   处理器   过滤器  格式器

如何编写一个日志记录器？
记录文件得知道把文件放到哪里，控制台要不要打印，文件要不要打印，两种打印的格式有没有区别
控制台打印的日志级别，文件打印的日志级别
'''


import logging
import logging.handlers


# 创建格式器
format = '%(asctime)s %(levelname)s %(message)s'
fmt = logging.Formatter(format)

#创建记录器,并设置 level
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)



ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(fmt)

fh = logging.handlers.TimedRotatingFileHandler('test1.log', when='d', interval=1)
fh.setLevel(logging.DEBUG)
fh.setFormatter(fmt)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("test")