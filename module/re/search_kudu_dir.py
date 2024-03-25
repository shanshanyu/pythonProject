# 2024/3/20 22:19
'''
把kudu的dir参数的值提取出来

desc：先用requests获取内容localhost:8050/varz的内容->然后用正则来匹配到 fs_data_dirs
'''

import requests
import re
import subprocess
import os


def main():
    response = requests.get('http://localhost:8050/varz')
    if response.status_code != 200:
        return ''

    fs_data_dir = re.search(r'--fs_data_dirs=([^\n]+)',response.content.decode()).group(1)
    fs_data_dir_lst = fs_data_dir.split(',')
    all_meta_size = ''
    for tmp_dir in fs_data_dir_lst :
        tmp_dir = os.path.join(tmp_dir, 'data')
        sudo_cmd = '''sudo su -c "find %s -name '*.metadata' -type f -exec du -c {} +|grep total"|awk '{sum += $1} END{print sum}' ''' % tmp_dir
        result = subprocess.run(sudo_cmd, capture_output=True, text=True,shell=True)
        all_meta_size += result.stdout.split()[0]
    print(all_meta_size)

if __name__ == '__main__':
    main()


