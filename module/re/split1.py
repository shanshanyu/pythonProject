'''
create_time: 2024/4/7 16:49
author: yss
version: 1.0

'窗前明月光，疑是地上霜。举头望明月，低头思故乡。'

分隔这首古诗,通过正则的 split 方法来实现
'''
import re


def main():
    s1 = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    res = re.split(r'[，。]',s1)
    while '' in res:
        res.remove('')
    print(res)


if __name__ == '__main__':
    main()