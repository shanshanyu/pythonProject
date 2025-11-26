def search_index(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

'''
二分查找的边界：
>=  
>    => >=(x+1)
<=   => >=(x+1)-1
<    => >=x-1   
'''

class Solution:
    def searchRange(self, nums, target):
        left = search_index(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = search_index(nums, target+1)-1
        return [left, right]



def main():
    s = Solution()
    ret = s.searchRange([5, 7, 7, 8, 8, 8, 9], 8)  #找到小于 target 的第一个数
    print(ret)


if __name__ == '__main__':
    main()



