'''
create_time: 2023/5/31 13:22
author: yss
version: 1.0
'''

#记录用户登录日志
import logging
from datetime import datetime

#初始化日志记录器
def get_logger(logname):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fmt = logging.Formatter()
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    return logger


if __name__ == '__main__':
    username = input('输入用户名：')
    password = input('输入密码：')

    if username == 'admin' and password == 'admin':
        print('登录成功')
        logger = get_logger('user_login')
        logger.info(f'用户名：{username}，登录时间：{datetime.now()}')
    else:
        print('用户名或密码不正确')
