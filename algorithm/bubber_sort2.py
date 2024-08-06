'''
create_time: 2023/6/18 08:55
author: yss
version: 1.0
'''
lst = [5,4,3,2,1,6,7,8,10,9]

len_lst = len(lst)

def bubber_sort(lst,length):
    i = 0
    while i < length:
        j = 0
        while j < length-1:  #如果每次都遍历整个列表，依然可以实现排序，只是多计算了后面已经排序的数
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]  #python 中可以用这种方式交换两个数的值
            j += 1
        i += 1

if __name__ == '__main__':
    bubber_sort(lst,len(lst))
    for i in lst:
        print(i)