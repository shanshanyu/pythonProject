class Solution:
    def twoSum(self, nums, target) :
        nums.sort()
        l = 0
        r = len(nums)-1
        res = []
        while l < r:
            if nums[l] + nums[r] == target:
                res.append(l)
                res.append(r)
                return res
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
            print(l,r)
        return res

def main():
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))

if __name__ == '__main__':
    main()
