from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        '''
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
        s = "abcabcbb"  3
        '''
        left = 0
        ans = 0
        cnt = Counter()  #用hashmap记录字符的个数
        for right, char in enumerate(s):
            cnt[char] += 1
            while cnt[char] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans



def main():
    s = Solution()
    ret = s.lengthOfLongestSubstring("abc")
    print(ret)

if __name__ == '__main__':
    main()