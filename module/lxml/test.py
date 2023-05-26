'''
create_time: 2023/5/24 18:40
author: yss
version: 1.0
'''

import requests
from lxml import etree

res = requests.get('http://123.56.222.255:28106')
print(res)
print(type(res))

html = res.text
#print(html)

root_element = etree.HTML(html)
print(root_element,type(root_element))

for element in root_element:
    for  i in element:
        print(etree.tostring(i).decode())

