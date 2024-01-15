'''
create_time: 2024/1/11 17:51
author: yss
version: 1.0

一个标准的日志记录器，控制台的级别默认为 info，日志的默认级别为 debug，日志发送到程序目录 runtime 下

'''





import logging
import logging.handlers
import logging.config
import os
import datetime


MY_DIR = os.path.abspath(os.path.dirname(__file__))
RUNTIME_DIR = os.path.join(MY_DIR,'runtime')


class LoggerColouredFormatter(logging.Formatter):
    COLOR_OF_LEVEL = {
        'DEBUG' : '\033[94m',
        'INFO' : '\033[92m',
        'WARNING' : '\033[93m',
        'CRITICAL' : '\033[93m',
        'ERROR' : '\033[91m',
    }

    #子类重写父类构造方法
    def __init__(self,fmt):
        super().__init__(fmt)

    def format(self,record):
        '''
        把 record 中的 level 换成带颜色的
        :param record:
        :return:
        '''
        levelname = record.levelname
        levelname_color = LoggerColouredFormatter.COLOR_OF_LEVEL.get(levelname.upper()) + levelname + '\033[0m'
        record.levelname = levelname_color
        ret = logging.Formatter.format(self,record)
        record.levelname = levelname
        return ret


def init_logger(logger_name,log_dir=RUNTIME_DIR,console_level=logging.INFO):
    timestamp = datetime.datetime.now().strftime('%Y%m%d')
    log_path = '{}{}'.format(log_dir,timestamp) if log_dir.endswith('/') else '{}/{}'.format(log_dir,timestamp)
    log_path += '.log'

    # 创建格式器
    format = '%(asctime)s %(levelname)s %(message)s'
    fmt = logging.Formatter(format)

    #全局配置
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    #console 配置
    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    #传递一个 Formatter 对象给方法
    ch.setFormatter(LoggerColouredFormatter(format))   #终端输出的时候要显示颜色,改一下 level 的颜色

    #file 配置
    fh = logging.handlers.TimedRotatingFileHandler(log_path,when='d',interval=1)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    logger.addHandler(ch)
    # logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    logger = init_logger(__name__)
    logger.info('info msg')
    logger.debug('debug msg')