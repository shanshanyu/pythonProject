class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int):
        '''
        给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
        nums = [10,5,2,6], k = 100

        下面的程序能计算出来，不过时间复杂度是 O(n^2)
        '''
        n = len(nums)
        ans = 0
        for left,x in enumerate(nums):
            right = left
            s = x
            while  s < k and right < n:
                ans += 1
                right += 1
                if right < n:
                    s *= nums[right]
        return ans


def main():
    s = Solution()
    ret = s.numSubarrayProductLessThanK([1,2,3,4], 100)
    print(ret)


if __name__ == '__main__':
    main()

