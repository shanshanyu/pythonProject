import sys
class Solution:
    '''
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    解：利用左右两个数组，分别存储每个格子能存最多水的高度，然后就能计算出每个格子最多能存多少水
    '''
    def trap(self, height):
        n = len(height)
        pre_max = [0]*n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1],height[i])

        suf_max = [0]*n
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1],height[i])

        count = 0
        for h,pre,suf in zip(height,pre_max,suf_max):
            count += min(pre,suf)-h

        return count


def main():
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))


if __name__ == '__main__':
    main()
