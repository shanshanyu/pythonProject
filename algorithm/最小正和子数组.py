class Solution:
    def minimumSumSubarray(self, nums, l: int, r: int):
        '''
        给你一个整数数组 nums 和 两个 整数 l 和 r。你的任务是找到一个长度在 l 和 r 之间（包含）且和大于 0 的 子数组 的 最小 和。
        返回满足条件的子数组的 最小 和。如果不存在这样的子数组，则返回 -1。
        子数组 是数组中的一个连续 非空 元素序列。

        输入： nums = [3, -2, 1, 4], l = 2, r = 3
        输出： 1

        '''
        ans = 10000
        for i in range(l,r+1):
            for j in range(len(nums)):
                if j+i >= len(nums):
                    continue
                cnt = sum(nums[j:j+i])
                if cnt > 0:
                    ans = min(ans, cnt)
        return ans if ans != 10000 else -1



def main():
    s = Solution()
    ret = s.minimumSumSubarray([3, -2, 1, 4],2,3)
    print(ret)




if __name__ == '__main__':
    main()