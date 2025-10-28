class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int):
        '''
        给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
        nums = [10,5,2,6], k = 100

        '''
        if k <= 1:  # 题目描述有问题，正整数数组，而不是整数数组
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
    s = Solution()
    ret = s.numSubarrayProductLessThanK([10,5,2,6], 100)
    print(ret)


if __name__ == '__main__':
    main()

