'''
create_time: 2023/5/28 21:41
author: yss
version: 1.0
'''

#requests 是一个http请求库

import requests
#发送一个 http 请你去
x = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
x.encoding = 'utf-8'
#print(x.content)
#print(x.text)
print(x.json())