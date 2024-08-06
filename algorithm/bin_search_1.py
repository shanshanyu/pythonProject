'''
create_time: 2023/6/15 18:21
author: yss
version: 1.0
'''

lst = [5,4,3,2,1,5,6]
lst_len = len(lst)

def bin_search(num,lst,lst_len):  #lst 要求有序，并且是升序
    print(lst)
    high = lst_len-1
    low = 0

    while lst[low] <= lst[high]:
        mid = int((high+low)/2)
        if lst[mid] < num:
            low = mid+1
        elif lst[mid] > num:
            high = mid-1
        else:
            return mid
    return -1

if __name__ == '__main__':
    res = bin_search(6,sorted(lst),lst_len)
    print(res)
