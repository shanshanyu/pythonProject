'''
create_time: 2024/3/28 11:34
author: yss
version: 1.0

desc:通过 requests 模块获取 url 的内容，然后通过 json 解析
'''

import requests
import json


def main():
    resp = requests.get('https://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    print(data_model)


if __name__ == '__main__':
    main()
