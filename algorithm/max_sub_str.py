'''
Data: 2024/8/12 21:21
Author: yss
Desc: 定长子串中元音的最大数目
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。
'''

'''
tips: 使用双指针解决  （定长滑动窗口）
'''

def max_sub_str(s,k):
    '''
           通过双指针解决
           先取最左边的k个字符
           然后判断元音字母的个数，和之前保存的max_count比较取大
           右指针加1，左指针加1
           判断左指针指向的字符和右指针指向的字符是否是元音字母
           判断元音字母的个数，和之前保存的max_count比较取大
    '''
    am_str = 'aeiou'
    ans = 0
    for i in s[0:k]:
        if i in am_str:
            ans += 1

    tmp_ans = ans
    left = 0
    length = len(s)
    for right in range(k, length):
        if s[right] in am_str and s[left] not in am_str:
            tmp_ans += 1
        elif s[right] not in am_str and s[left] in am_str:
            tmp_ans -= 1

        left += 1

        ans = max(ans, tmp_ans)

    return ans


def main():
    s = 'leecode'
    k = 3
    ret = max_sub_str(s,k)
    print(ret)


if __name__ == '__main__':
    main()

