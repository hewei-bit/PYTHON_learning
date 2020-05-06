"""
680. Valid Palindrome II (Easy)
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                case1, case2 = s[l:r], s[l + 1:r + 1]
                return case1 == case1[::-1] or case2 == case2[::-1]
            l, r = l + 1, r - 1
        return True


aaa = 'aabaca'
obj = Solution().validPalindrome(aaa)
print(obj)
