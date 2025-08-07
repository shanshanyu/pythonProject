

def main():
    try:
        with open('craps.py','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError as e:
        print('文件未找到')
    except UnicodeDecodeError as e:
        print('文件编码错误')
    except IOError as e:
        print('文件读写出错')


if __name__ == '__main__':
    main()
