'''
create_time: 2024/3/27 17:35
author: yss
version: 1.0


将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）

打开 3 个文件->遍历1~9999,1~99 范围的写 a,100~999 范围的写 b...->关闭文件
'''


def get_primer(num):
    '''
    判断一个数是不是质数，质数的范围 2,3,5,7...
    :param num:
    :return:
    '''
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    flag = True
    for j in range(2, int(num/2)+1):  # for(i = 2; i < j/2;i++)
        if num % j == 0 :
            flag = False
            break
    if flag :
        return True
    else:
        return False
def main():
    f_a = None
    f_b = None
    f_c = None
    try:
        f_a = open('./a.txt','w')
        f_b = open('./b.txt','w')
        f_c = open('./c.txt','w')
        for i in range(1,10000):
            if not get_primer(i):
                continue

            if i <= 99:
                f_a.write(str(i)+'\n')
            elif i <= 999:
                f_b.write(str(i)+'\n')
            elif i <= 9999:
                f_c.write(str(i)+'\n')
    except Exception as e:
        print(e)
    finally:
        f_a.close()
        f_b.close()
        f_c.close()


def read_file(path):
    try:
        with open(path,'r',encoding='utf-8') as f:
            data = f.read()
            print(data)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
    read_file('./a.txt')

