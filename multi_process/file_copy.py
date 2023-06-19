'''
create_time: 2023/6/17 22:35
author: yss
version: 1.0
'''
#多进程实现目录 copy


import os
import multiprocessing

file_lst = []

def cp(src_dir,dst_dir):
    pass


def copy_file(src_dir,dst_dir):
    #判断目标文件夹是否存在，如果不存在则创建
    try:
        os.mkdir(dst_dir)
    except:
        print('dst_dir exist,no need create')

    #读取源文件目录，把读到的文件放到 file_lst
    global file_lst
    file_lst = os.listdir(src_dir)

    #创建 5 个子进程
    for i in range(5):
        p = multiprocessing.Process(target=cp(src_dir,dst_dir))
        p.start()


    #每个进程从列表中取出一个目录复制，对列表的处理要加锁，列表是共享资源，列表为空退出
    pass


if __name__ == '__main__':
    pass