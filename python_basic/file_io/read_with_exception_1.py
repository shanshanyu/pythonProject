'''
create_time: 2024/3/27 17:29
author: yss
version: 1.0
'''
def main():
    f = None
    try:
        #with 块可以不用主动关闭文件
        with open('./test.txt','r',encoding='gb2312') as f:
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
        print('over')

if __name__ == '__main__':
    main()
