"""
编程之美 3.1
给定两个字符串 s1 和 s2，要求判定 s2 是否能够被 s1 做循环移位得到的字符串包含。

s1 进行循环移位的结果是 s1s1 的子字符串，因此只要判断 s2 是否是 s1s1 的子字符串即可。
"""


class Solution:
    def stringloopcontain(self, a: str, b: str):
        a = a * 2
        if b in a:
            return True
        else:
            return False


aaa = "abcd"
bbb = "da"

obj = Solution()
ans = obj.stringloopcontain(aaa, bbb)
print(ans)
