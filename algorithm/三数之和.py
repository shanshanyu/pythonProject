class Solution:
    def threeSum(self, nums):
        '''
        把一个数固定，剩下的两个数用相向双指针
        '''
        res = []
        length = len(nums)
        nums.sort() # nums 排序
        for i in range(length-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                if nums[j]+nums[k]+nums[i] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j]+nums[k]+nums[i]>0:
                    k -= 1
                else:
                    j += 1

        return res



def main():
    s = Solution()
    nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    print(s.threeSum(nums))


if __name__ == '__main__':
    main()