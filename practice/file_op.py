
def main():

    f = None
    try:
        f = open('1.py','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件未找到')
    except UnicodeDecodeError:
        print('文件解码失败')
    finally:
        f.close()

if __name__ == '__main__':
    main()
