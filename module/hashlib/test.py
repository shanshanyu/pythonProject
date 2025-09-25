'''hashlib'''

import hashlib

def md5(data_string):
    '''md5加密'''
    obj = hashlib.md5()  # 创建hash 对象
    obj.update(data_string.encode('utf-8'))  # 更新 hash 对象
    return obj.hexdigest()  # 返回摘要



def main():
    input_str = input('输入一个字符串：')
    ret = md5(input_str)
    print(ret)


if __name__ == '__main__':
    main()