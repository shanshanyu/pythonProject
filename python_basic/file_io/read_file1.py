'''
create_time: 2023/11/16 11:32
author: yss
version: 1.0
'''

def main():
    f = None
    try:
        f = open('test.txt','r',encoding='utf-8')
        #一次性读取整个文件
        data = f.read()
    except FileNotFoundError:
        print('文件没找到')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件解码错误')
    else:
        print(data)
    finally:
        f.close()


if __name__ == '__main__':
    main()

