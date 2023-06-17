'''
create_time: 2023/6/16 14:06
author: yss
version: 1.0
多线程查找 nginx 日志：
1. 输入时间以及查找的表达式，一共需要两个参数，第一个参数是时间
2. 拼接命令
3. 获取所有的 nginx 主机
4. 在所有的机器上执行命令并获取结果
'''

import argparse
import re
import os



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='find access log')
    parser.add_argument('time',help='input time,like: 2023061509,仅支持小时')
    parser.add_argument('fmt',help='input condition,like: xxxxxx   distinct_id 等')
    args = parser.parse_args()
    print(args.time,args.fmt)

    re = re.compile('\d{10}')
    if not re.match(args.time):
        print("时间格式输入错误，应输入类似：2023061509，仅支持小时")
        exit(1)

    decoding ='${SENSORS_DATAFLOW_HOME}/extractor/bin/sa-nginx-log-translator'











