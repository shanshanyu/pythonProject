'''
create_time: 2023/11/15 18:11
author: yss
version: 1.0
'''


def main():
    try:
        with open('test.txt', 'r') as f :
            data = f.read()
            print(data)
    except Exception as e:
        print(e)
    else:
        print("程序执行成功了")
    finally:
        print("打扫一下")


if __name__ == '__main__':
    main()