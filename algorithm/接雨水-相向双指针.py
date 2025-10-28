class Solution:
    '''
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    解：利用左右两个数组，分别存储每个格子能存最多水的高度，然后就能计算出每个格子最多能存多少水
    时间复杂度 O(N)
    空间复杂度 O(1)
    '''
    def trap(self, height):
        n = len(height)
        pre_max = 0
        suf_max = 0
        left = 0
        right = n - 1
        res = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                res += pre_max - height[left]
                left += 1
            else:
                res += suf_max - height[right]
                right -= 1
        return res



def main():
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))


if __name__ == '__main__':
    main()
