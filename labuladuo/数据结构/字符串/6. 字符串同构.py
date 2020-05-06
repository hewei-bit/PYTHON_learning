"""
205. Isomorphic Strings (Easy)

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true

"""

'''方法一'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]


'''方法二'''
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        L = []
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in L:
                    return False
                L.append(t[i])
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True


'''方法三'''
class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        preIndexs = {}
        preIndext = {}
        for i in range(len(s)):
            preIndexs[s[i]] = i + 1
            preIndext[t[i]] = i + 1
        for i in range(len(s)):
            if preIndext[t[i]] != preIndexs[s[i]]:
                return False
        return True


s = "paper"
t = "title"
obj = Solution3()
ans = obj.isIsomorphic(s, t)
print(ans)
