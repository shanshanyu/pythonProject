'''
create_time: 2023/5/24 17:53
author: yss
version: 1.0
'''

import logging
import requests


logger = logging.getLogger('del_tencent_email')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(fmt)
logger.addHandler(ch)


class DelTencentEmail(object):
    def __init__(self):
        self.host = 'https://exmail.qq.com'



    def del_tencent_email(self):
        cnt = 0
        while True:
            for i in range(100):
                params = {'filetype' : '', 'showattachtag' : '', 'listmode' : '', 'flag' : '', 'fun' : '', 'category' : '',
                  'searchmode' : '', 'stype' : '', 'grpid' : '', 'AddrID' : '', 'ftype' : '', 'page' : i,
                  'folderid' : '1', 'sid' : self.sid, 's' : 'inbox'}

                str_html = requests.get(url='https://exmail.qq.com/cgi-bin/mail_list',params=params)
                email_info = self.get_email_info_by_strhtml(str_html)
                self.del_email_by_emails_info_list(*email_info)



    def get_email_info_by_strhtml(self,str_html):
        email_info = []
        email_dict = {}
        email_id = x

    def del_email_by_emails_info_list(self):
        pass

if __name__ == '__main__':
    d = DelTencentEmail()


