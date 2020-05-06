"""
242. Valid Anagram (Easy)
"""


'''Solution-1'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0
        new = [0 for i in range(26)]
        i = 0
        for i in range(len(s)):
            new[ord(s[i]) - ord('a')] += 1
            new[ord(t[i]) - ord('a')] -= 1
        i = 0
        for i in range(26):
            if new[i] != 0:
                return False
        return True


'''Solution-2'''
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


a1 = 'abc'
a2 = 'bca'
obj = Solution()
ooo = obj.isAnagram(a1, a2)
print(ooo)
