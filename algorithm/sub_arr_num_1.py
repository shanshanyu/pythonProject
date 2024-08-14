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
    for right, x in enumerate(nums):
        s *= x
        '''
        写法一：
        加了 left<right后的执行情况：
        第一个数比k大，什么都没做
        第二个数还是比k大，把第一个数除掉了
        第三个数还是比k大，把第一个数除掉了。
        写法二：
        不加left<right
        第一个数比k大，直接除掉了，left+1，left>right
        right-left+1 = 0
        代码会简洁一点
        '''
        # while s >= k and left < right:  #可以不需要 left < right
        #     s /= nums[left]
        #     left += 1

        # if s < k:
        #     ans += right-left+1
        while s >= k:
            s /= nums[left]
            left += 1

        ans += right - left + 1

    return ans


def main():
    nums = [10, 5, 2, 6]
    k = 100
    ret = sub_arr_num(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
