'''
create_time: 2024/5/6 14:29
author: yss
version: 1.0

desc: 获取指定花的花语
'''


import requests


def main():
    resp = requests.get('https://apis.tianapi.com/huayu/index?key=d3838c975aed394cad6c84d393162a27&word=玫瑰花')
    data = resp.json()
    if data['code'] == 200:
        print(data['result'].get('flowerlang'))


if __name__ == '__main__':
    main()
