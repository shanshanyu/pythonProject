'''
create_time: 2023/6/25 13:35
author: yss
version: 1.0
'''
'''
create_time: 2023/6/17 22:35
author: yss
version: 1.0
'''

#多进程实现文件 copy，没有问题
import os
import os.path
import multiprocessing
import shutil

lock = multiprocessing.Lock()

def cp(src_dir,dst_dir,queue):
    # 每个进程从列表中取出一个目录复制，对列表的处理要加锁，列表是共享资源，列表为空退出   进程同步
    while True:

        lock.acquire()
        #print('{} lock'.format(multiprocessing.current_process().name))
        if queue.empty():
            lock.release()
            break
        src_filename = queue.get()
        #print(src_filename)
        src_file = os.path.join(src_dir, src_filename)
        #print('{}'.format(multiprocessing.current_process().name),src_file)

        dst_filename = src_filename
        dst_file = os.path.join(dst_dir,dst_filename)
        #print(dst_file)

        #print('{} unlock'.format(multiprocessing.current_process().name))
        lock.release()
        if os.path.isdir(src_file):
            shutil.copytree(src_file,dst_file)
        else:
            shutil.copy(src_file,dst_file,follow_symlinks=False)
        print('{} copy success.'.format(src_file))





def copy_file(src_dir,dst_dir,pr_num):
    #判断目标文件夹是否存在，如果不存在则创建
    try:
        os.mkdir(dst_dir)
    except:
        print('dst_dir exist,no need create')

    queue = multiprocessing.Queue()

    #读取源文件目录，把读到的文件放到 queue

    for i in os.listdir(src_dir):
        queue.put(i)

    #创建 5 个子进程
    for i in range(pr_num):
        p = multiprocessing.Process(target=cp,args=(src_dir,dst_dir,queue),name=str(i))
        p.start()


if __name__ == '__main__':
    src_dir = input('input src path: ')
    dst_dir = input('input dst path: ')

    copy_file(src_dir,dst_dir,5)