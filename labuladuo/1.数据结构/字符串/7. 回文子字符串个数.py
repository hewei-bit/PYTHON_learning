"""
647. Palindromic Substrings (Medium)

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".

"""


class Solution:

    def countSubstrings(self, s: str) -> int:
        def get_Center(s: str, l: int, r: int):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        n = len(s)
        sum1 = 0
        for i in range(len(s)):
            count_even = get_Center(s, i, i)
            count_odd = get_Center(s, i, i + 1)
            sum1 = sum1 + count_even + count_odd
        return sum1


aaa = "abc"
obj = Solution()
ans = obj.countSubstrings(aaa)
print(ans)
