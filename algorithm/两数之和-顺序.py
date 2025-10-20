class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        res = []
        while left < right:
            if numbers[left]+numbers[right] == target:
                res.append(left+1)
                res.append(right+1)
                break  # 找到了直接 break 退出循环
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
        return res


def main():
    s = Solution()
    print(s.twoSum([2,7,11,15],9))

if __name__ == '__main__':
    main()
