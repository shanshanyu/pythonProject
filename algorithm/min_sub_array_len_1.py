# 2024/8/10  15:09
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
    滑动窗口问题，使用双指针试试
    '''
    n = len(nums)  # 数组长度
    left = 0  # 左指针
    s = 0  # 和
    ans = n+1  # 初始化ans 为一个很大的值
    for right,x in enumerate(nums):  # i 是索引，x是值
        s += x  # 动右指针，把上一次的结果用起来
        while s - nums[left] >= target:
            s -= nums[left]
            left += 1
            ans = min(ans,right-left+1)

        if s >= target:
            ans = min(ans,right-left+1)

    return ans if ans < n+1 else 0


def main():
    lst = [1,2,3,4,5]
    ret = min_sub_array_len(15,lst)
    print(ret)


if __name__ == '__main__':
    main()