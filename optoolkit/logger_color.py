'''
create_time: 2024/1/11 10:48
author: yss
version: 1.0
'''
import logging
import logging.handlers
import datetime
import os


#获取脚本路径
MY_DIR = os.path.dirname(os.path.abspath(__file__))
RUNTIME_DIR = os.path.join(MY_DIR,'runtime')


class LoggerColouredFormatter(logging.Formatter):
    COLOR_OF_LEVEL = {
        'DEBUG': '\033[94m',
        'INFO': '\033[92m',
        'WARNING': '\033[93m',
        'CRITICAL': '\033[93m',
        'ERROR': '\033[91m',
    }

    def __init__(self, fmt):
        logging.Formatter.__init__(self, fmt) #调用父类的构造方法，创建的是一个 formatter 对象

    def format(self, record):
        levelname = record.levelname
        levelname_color = LoggerColouredFormatter.COLOR_OF_LEVEL[levelname.upper()] + levelname + '\033[0m'
        record.levelname = levelname_color
        ret = logging.Formatter.format(self, record)
        record.levelname = levelname
        return ret


def init_logger(logger_name, log_dir=RUNTIME_DIR, console_level=logging.INFO):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    log_name = '{}_{}.log'.format(logger_name, timestamp)
    log_path = '{}{}'.format(log_dir, log_name) if log_dir.endswith('/') else '{}/{}'.format(log_dir, log_name)
    file_format = '%(asctime)s %(levelname)s %(message)s'

    # global config
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # console config
    console = logging.StreamHandler()
    console.setLevel(console_level)
    console.setFormatter(LoggerColouredFormatter(file_format))
    logger.addHandler(console)

    # log file rotate config
    fa = logging.handlers.TimedRotatingFileHandler(log_path, when='D', interval=1, backupCount=7)
    fa.setLevel(logging.DEBUG)
    formater = logging.Formatter(file_format)
    fa.setFormatter(formater)
    logger.addHandler(fa)

    return logger

if __name__ == '__main__':
    logger = init_logger(__name__)
    logger.info('info log')