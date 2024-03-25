'''
create_time: 2024/3/21 10:18
author: yss
version: 1.0

os.walk 方法的使用

生成目录树中的文件名，方式是按上->下或下->上顺序浏览目录树。
'''


import os
import subprocess


def main():
    sudo_cmd = ['sudo','su','-']
    try:
        subprocess.run(sudo_cmd)
    except subprocess.CalledProcessError as e:
        print(e)
    for i,j,k in  os.walk('/sensorsdata/rnddata00/kudu/tserver_data'):
        print(i,j,k)



if __name__ == '__main__':
    main()