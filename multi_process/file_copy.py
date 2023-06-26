'''
create_time: 2023/6/17 22:35
author: yss
version: 1.0
'''
#多进程实现目录 copy

#这个程序是错误的，因为用了全局变量来做进程间同步


import os
import os.path
import multiprocessing
import fcntl
import shutil
import time


file_lst = []

#创建一个文件用作文件锁参数
f = open('/tmp/file_copy','w')  #获取到一个文件对象


def cp(src_dir,dst_dir):
    # 每个进程从列表中取出一个目录复制，对列表的处理要加锁，列表是共享资源，列表为空退出   进程同步
    while True:

        fcntl.lockf(f.fileno(), fcntl.LOCK_EX)  # 加锁
        print('{} lock'.format(multiprocessing.current_process().name))
        print(id(f))
        global file_lst
        print(id(file_lst))
        time.sleep(3)
        if len(file_lst) == 0:
            fcntl.lockf(f.fileno(),fcntl.LOCK_UN)
            break
        src_filename = file_lst.pop()
        print(src_filename)
        src_file = os.path.join(src_dir, src_filename)
        print('{}'.format(multiprocessing.current_process().name),src_file)

        dst_filename = src_filename
        dst_file = os.path.join(dst_dir,dst_filename)
        print(dst_file)
        print(file_lst)
        print('{} unlock'.format(multiprocessing.current_process().name))
        fcntl.lockf(f.fileno(), fcntl.LOCK_UN)  # 解锁
        if os.path.isdir(src_file):
            shutil.copytree(src_file,dst_file)
        else:
            shutil.copy(src_file,dst_file)
        print('{} copy success.'.format(src_file))





def copy_file(src_dir,dst_dir,pr_num):
    #判断目标文件夹是否存在，如果不存在则创建
    try:
        os.mkdir(dst_dir)
    except:
        print('dst_dir exist,no need create')

    #读取源文件目录，把读到的文件放到 file_lst
    global file_lst
    file_lst = os.listdir(src_dir)

    #创建 5 个子进程
    for i in range(pr_num):
        p = multiprocessing.Process(target=cp,args=(src_dir,dst_dir),name=str(i))
        p.start()


if __name__ == '__main__':
    src_dir = input('input src path: ')
    dst_dir = input('input dst path: ')

    copy_file(src_dir,dst_dir,5)