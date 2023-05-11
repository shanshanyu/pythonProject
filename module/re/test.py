'''
create_time: 2023/5/10 17:49
author: yss
version: 1.0
'''

print("\\")

import re

reg = re.compile('[1-9][0-9]{0,2}(\.[0-9]{1,3}){3}')  #匹配 ip
result = reg.match('256.168.1.1')
print(result)

#25[0-5]| 2[0-4]\d
#p = re.compile('^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9])(\.25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d){3}$')  #匹配 200~255
#
p = re.compile('^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9])(\.25[0-5]|\.2[0-4]\d|\.1\d\d|\.[1-9]\d|\.\d){3}$')
result = p.match('192.255.255.255')
print(result)

p = re.compile('^(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)')  #099 也能匹配上
result = p.match('099')
print(result)