'''
create_time: 2024/1/10 15:59
author: yss
version: 1.0
'''

import sys
import logging
import logging.handlers
import datetime


class Logger:
    def __init__(self, level='info',filename=__name__, log_name='runtime.log'):
        self.level = level
        # 在这里定义StreamHandler，可以实现单例， 所有的logger()共用一个StreamHandler
        self.console_handler = logging.StreamHandler(sys.stdout)
        # self.fh = logging.FileHandler(filename, encoding='utf-8')
        # 日志文件按天进行保存，每天一个日志文件
        self.filename = filename
        self.file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_name, when='D', backupCount=1, encoding='utf-8')
        self.level_relations = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        self.level_color = {
            'error': "31",
            'info': "32",
            'warning': "33",
            'debug': "34",
            'critical': "35"
        }
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations.get(self.level, 'info'))

    def debug(self, message, lineno=None):
        """debug"""
        self.font_color('debug', lineno)
        self.logger.debug(message)

    def info(self, message, lineno=None):
        """info"""
        self.font_color('info', lineno)
        self.logger.info(message)

    def warning(self, message, lineno=None):
        """warning"""
        self.font_color('warning', lineno, )
        self.logger.warning(message)

    def error(self, message, lineno=None):
        """error"""
        self.font_color('error', lineno)
        return self.logger.error(message)

    def critical(self, message, lineno=None):
        """critical"""
        self.font_color('critical', lineno, full=True)
        self.logger.critical(message)

    def font_color(
            self,
            level,
            lineno=None,
            file=None,
            full=False):
        """
        不同级别的日志输出不同的颜色,
        full: True，日志内容全部呈现某一颜色
        full: False， levelname呈现某一颜色
        """
        log_color = self.level_color.get(level, 37)
        file_fmt = f'%(asctime)s {self.filename}\
[line:%(lineno)d - %(levelname)s: %(message)s'

        if full:
            log_fmt = f'\033[0;{log_color}m%(asctime)s %(filename)s\
[line:%(lineno)d %(levelname)s %(message)s\033[0m'
            log_fmt = f"\033[0;{log_color}m%(asctime)s %(levelname)s \
%(message)s\033[0m"
        else:
            if lineno:
                log_fmt = f"%(asctime)s \
\033[{log_color}m%(levelname)s\033[0m %(message)s"
                if file:
                    file_fmt = f'%(asctime)s {file}[line:{lineno} \
- %(levelname)s: %(message)s'
                else:
                    file_fmt = f'%(asctime)s {self.filename}[line:{lineno} \
- %(levelname)s: %(message)s'
            else:
                log_fmt = f"%(asctime)s \
\033[{log_color}m%(levelname)s\033[0m %(message)s"
        con_formatter = logging.Formatter(log_fmt)
        file_formatter = logging.Formatter(file_fmt)
        self.console_handler.setFormatter(con_formatter)
        self.file_handler.setFormatter(file_formatter)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)


if __name__ == '__main__':
    log_name = f"hdfs_import_tools_{datetime.date.today().strftime('%Y-%m-%d')}.log"  # 日志文件名
    logger = Logger(filename=__file__,log_name=log_name)
    logger.info('info msg')
    logger.debug('debug msg')
    logger.error('error msg')

