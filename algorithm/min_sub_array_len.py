# 2024/8/10  12:48
'''
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''

'''
子数组，说明是连续的，不能先排序
'''


def min_sub_array_len(target,nums):
    '''
    暴力解法，时间复杂度 o(n^2)
    '''
    all = sum(nums)
    if all < target:
        return 0

    length = len(nums)
    for i in range(1, length + 1):  # 子数组长度
        for j in range(0, length):
            new_list = nums[j:j + i]
            if sum(new_list) >= target:
                return i


def main():
    lst = [12,28,83,4,25,26,25,2,25,25,25,12]
    ret = min_sub_array_len(213,lst)
    print(ret)


if __name__ == '__main__':
    main()

