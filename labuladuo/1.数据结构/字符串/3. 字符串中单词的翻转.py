"""
151. Reverse Words in a String
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

"""
'''方法一'''


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


'''方法二'''


class Solution2:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = ""
        i, j = len(s) - 1, len(s)
        while i > 0:
            if s[i] == " ":
                res += s[i + 1:j] + ' '
                while s[i] == ' ':
                    i -= 1
                j = i + 1
            i = i - 1
        return res + s[:j]


ans = "I am hewei"
obj = Solution()
aaa = obj.reverseWords(ans)
print(aaa)
