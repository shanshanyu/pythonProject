'''
create_time: 2024/5/10 14:20
author: yss
version: 1.0

desc: 测试当前系统缺少哪些 cpu flag
'''
import subprocess
import sys


def cpu_flag_test():
    flag_require = ['avx2', 'avx', 'ssse3', 'sse4', 'sse4_2', 'popcnt']
    flag_require = set(flag_require)
    output = []

    try:
        test_cmd = "lscpu|grep Flags|awk -F ':' '{print $2}'"
        complete_process = subprocess.run(test_cmd,shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if complete_process.returncode != 0:
            print('检测命令失败')
            print(complete_process.stderr)
            sys.exit(1)
        output = complete_process.stdout.strip().split()
        output = set(output)

    except Exception as e:
        print(e)

    tmp_set = flag_require.difference(output)

    if len(tmp_set) != 0:
        print('缺少如下flag:')
        print(list(tmp_set))


if __name__ == '__main__':
    cpu_flag_test()

