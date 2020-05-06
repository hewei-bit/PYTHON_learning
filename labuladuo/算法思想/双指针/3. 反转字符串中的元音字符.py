"""

345. Reverse Vowels of a String (Easy)
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"
示例 2:
输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        res = []
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i, k in enumerate(s):
            if k in vowels:
                while s[j] not in vowels:
                    j -= 1
                res.append(s[j])
                j -= 1
            else:
                res.append(k)
        return ''.join(res)

    def reverseVowels2(self, s: str) -> str:
        res = list(s)
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            if res[i] in vowels and res[j] in vowels:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
            if res[i] not in vowels:
                i += 1
            if res[j] not in vowels:
                j -= 1
        return ''.join(res)


aaa = "leeched"

obj = Solution().reverseVowels2(aaa)
print(obj)
