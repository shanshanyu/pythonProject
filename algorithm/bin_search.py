'''
create_time: 2023/6/15 18:06
author: yss
version: 1.0
'''
#二分查找


def bin_search(start,end,num):
    if start > num or end < num:
        return -1

    mid = (start+end)/2
    if num < mid:
        return bin_search(start,mid-1,num)
    elif num > mid:
        return bin_search(mid+1,end,num)
    elif num == mid:
        return 0
    else:
        return -1


if __name__ == '__main__':
    res = bin_search(5,10,9)
    if res == 0:
        print('找到了')
    elif res == -1:
        print('没找到')
    else:
        print('出错了')
