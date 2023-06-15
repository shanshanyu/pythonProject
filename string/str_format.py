'''
create_time: 2023/6/6 18:13
author: yss
version: 1.0
'''

import os
collect_number = 100000


web_log_dir = os.path.join('/tmp','web')
print(web_log_dir)

web_log_path = os.path.join(web_log_dir,'web.log')
print(web_log_path)

cmd = 'tail -n {} {} >/tmp/.{}-{}'.format(collect_number,web_log_path,'abc','web.log')
print(cmd)
exit(0)