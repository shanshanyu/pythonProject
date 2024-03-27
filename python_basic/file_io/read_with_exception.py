'''
create_time: 2024/3/27 17:15
author: yss
version: 1.0

file io 在有异常的情况下，捕获异常
'''


def main():
    f = None
    try:
        f = open('./test.txt','r',encoding='gb2312')
        data = f.read()
        print(data)
    except FileNotFoundError:
        #文件未找到
        print('文件未找到')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('读取文件时未知编码')
    else:
        print('操作正常')
    finally:
        #需要在 finally 块中关闭文件
        f.close()
        print('文件关闭')

if __name__ == '__main__':
    main()
