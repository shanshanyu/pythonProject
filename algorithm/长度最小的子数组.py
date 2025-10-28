class Solution:
    '''
    给定一个含有 n 个正整数的数组和一个正整数 target 。
    找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0
    '''
    def minSubArrayLen(self, target: int, nums):
        n = len(nums)
        ans = n+1
        left = 0  # 左指针
        s = 0
        for right,x in enumerate(nums):
            s += x
            while s-nums[left] >= target:
                s -= nums[left]
                left += 1  # 左指针右移

            if s >= target:
                ans = min(ans, right-left+1)

        return ans if ans < n+1 else 0





def main():
    s = Solution()
    print(s.minSubArrayLen(7,[2,3,1,2,4,3]))


if __name__ == '__main__':
    main()
