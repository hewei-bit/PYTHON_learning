"""
744. Find Smallest Letter Greater Than Target (Easy)
给定一个只包含小写字母的有序数组letters 和一个目标字母 target，
寻找有序数组里面比目标字母大的最小字母。

在比较时，数组里字母的是循环有序的。举个例子：

如果目标字母 target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
如果目标字母 target = 'n' 并且有序数组为 letters = ['m', 'z', 'c', 'f', 'j'] ，
则答案返回 'z' 。

示例：

输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

"""


class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        l, h = 0, len(letters) - 1
        while l < h:
            m = (l + h) // 2
            if letters[m] > target:
                h = m
            else:
                l = m + 1
        return letters[l] if letters[l] > target else letters[0]



letters = ["c", "f", "j"]
target = "c"
obj = Solution().nextGreatestLetter(letters, target)
print(obj)
