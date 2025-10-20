class Solution:
    '''
    计算两数之和
    方法的时间复杂度是 O(N^2)
    '''
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res


def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))

if __name__ == '__main__':
    main()