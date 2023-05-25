'''
create_time: 2023/5/25 09:43
author: yss
version: 1.0
'''

import imaplib

mail = imaplib.IMAP4_SSL('imap.exmail.qq.com',993)
mail.login('yushanshan@sensorsdata.cn','ZXcv1324!@#$')
mail.select()
mail.close()
mail.logout()