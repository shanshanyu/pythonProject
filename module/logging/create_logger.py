'''
create_time: 2023/3/29 09:58
author: yss
version: 1.0
'''
import logging
import logging.handlers

#创建记录器
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

#创建格式器
format = '%(asctime)s %(levelname)s %(message)s'
fmt = logging.Formatter(format)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(fmt)

fh = logging.handlers.TimedRotatingFileHandler('test1.log', when='d', interval=1)
fh.setLevel(logging.DEBUG)
fh.setFormatter(fmt)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("test")