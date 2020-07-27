"""
编程之美 2.17
将字符串向右循环移动 k 位。

将 abcd123 中的 abcd 和 123 单独翻转，得到 dcba321，然后对整个字符串进行翻转，得到 123abcd。
"""


class Solution:
    def stringcyclicshift(self, s: str, k: int):
        return s[-k:] + s[:-k]

class Solution2:
    def stringcyclicshift(self, s: str, k: int):
        return s[-k:] + s[:-k]

aaa = "abcd123"
k = 3
obj = Solution()
ans = obj.stringcyclicshift(aaa, k)
print(ans)
