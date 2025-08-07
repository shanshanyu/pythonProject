'''占用内存不超过1m'''

def main():
    try:
        with open('craps.py','rb') as f1,open('craps1.py','wb') as f2:
            data = f1.read(512)
            while data:
                f2.write(data)
                data = f1.read(512)
    except FileNotFoundError:
        print('文件未找到')
    except PermissionError:
        print('权限有问题')
    except UnboundLocalError:
        print('文件编码异常')


if __name__ == '__main__':
    main()