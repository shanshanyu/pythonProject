'''
create_time: 2024/3/7 11:47
author: yss
desc:  获得文件名的后缀名
version: 1.0

输入一个文件名(xx.xx)->获得 . 的索引->根据字符串的[] 访问
'''

def filename_suffix(filename):
    index = filename.rfind('.')  #这里可能没找到
    if 0 < index < len(filename)-1:
        return filename[index+1:]
    else:
        return ''
def main():
    res = filename_suffix('1.txt')
    print(res)

if __name__ == '__main__':
    main()




