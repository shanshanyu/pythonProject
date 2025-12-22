class Solution:
    '''
    整数数组 nums 按升序排列，数组中的值 互不相同 。
    在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    （下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。
    给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
    '''
    def search(self, nums, target: int) -> int:
        def is_bule(i):
            end = nums[-1]
            if nums[i] <= end:
                return target > end or nums[i] >= target
            else:
                return target > end and nums[i] >= target

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if is_bule(mid):
                right = mid-1
            else:
                left = mid+1

        if left == len(nums) or nums[left] != target:
            return -1
        return left



def main():
    s = [4,5,6,7,0,1,2]
    target = 0
    obj = Solution()
    ret = obj.search(s, target)
    print(ret)


if __name__ == '__main__':
    main()