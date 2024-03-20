# 2024/3/20 22:19
'''
把kudu的dir参数的值提取出来

desc：先用requests获取内容localhost:8050/varz的内容->然后用正则来匹配到 fs_data_dirs
'''

import requests
import re


def main():
    response = requests.get('http://localhost:8050/varz')
    if response.status_code != 200:
        return ''

    fs_data_path = re.search(r'--fs_data_dirs=([^\n]+)',response.content.decode())
    print(fs_data_path.group())

if __name__ == '__main__':
    main()


