'''
create_time: 2024/3/27 18:58
author: yss
version: 1.0

复制图片，图片是二进制的
'''

def main():
    try:
        with open('/Users/yushanshan/Desktop/a.png','rb') as f:
            data = f.read()


        with open('/Users/yushanshan/Desktop/b.png','wb') as f1:
            f1.write(data)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
