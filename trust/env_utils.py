'''
create_time: 2023/5/11 10:45
author: yss
version: 1.0
'''
import re
def check_ip(ip):
    #p = re.compile('^((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$')
    p = re.compile('^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9])(\.25[0-5]|\.2[0-4]\d|\.1\d\d|\.[1-9]\d|\.\d){3}$')
    if p.match(ip):
        return True
    else:
        return False