'''
Data: 2024/8/14 20:25
Author: yss
Desc: 乘积小于 K 的子数组

给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
'''

def sub_arr_num(nums,k):
    '''
    不定长滑动窗口  子数组个数
    [l,r] 中包含r的子数组个数是 r-l+1 个  [1,2]  1-0+1
    思路：
    利用双指针
    左指针指向0，右指针指向0
    如果s小于k，计算ans+= right-left+1
    如果s>=k,右移左指针
    '''
    if k <= 1:  # 如果 k<=1 直接返回，不用计算了
        return 0

    s = 1
    left = 0
    ans = 0
    for right,x in enumerate(nums):
        s *= x
        while s >= k:
            s /= nums[left]
            left += 1

        ans += right-left+1

    return ans


def main():
    nums = [10, 5, 2, 6]
    k = 100
    ret = sub_arr_num(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
