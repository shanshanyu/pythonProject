class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) -1
        area = 0
        while i < j:
            cur_area = (j-i)*min(height[i],height[j])  #面积
            area = max(area, cur_area)
            #什么时候移动？哪条线短就移动哪条
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return area


def main():
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))


if __name__ == '__main__':
    main()