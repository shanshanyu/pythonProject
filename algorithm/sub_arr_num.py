'''
Data: 2024/8/12 22:50
Author: yss
Desc: 乘积小于 K 的子数组

给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
'''


def sub_arr_num(nums,k):
    '''
           不定长滑动窗口  求子数组个数

           思路：
           双指针试试，不停的扩大子数组，直到不满足条件
           从满足条件 -> 不满足条件
           左指针为0，不停的向右扩充直到不满足条件
           '''
    # 这段代码执行超时了，还需要继续优化
    s = 0
    ans = 0
    length = len(nums)
    for left, x in enumerate(nums):
        s = x
        right = left
        while s < k and right < length:
            ans += 1
            right += 1
            if right < length:
                s *= nums[right]

    return ans


def main():
    nums = [10,5,2,6]
    k = 100
    ret = sub_arr_num(nums,k)
    print(ret)


if __name__ == '__main__':
    main()



