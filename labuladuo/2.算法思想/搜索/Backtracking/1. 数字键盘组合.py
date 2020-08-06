"""
17. Letter Combinations of a Phone Number (Medium)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        track = []
        if not digits or digits is None:
            return combinations
        self.doCombination(track, combinations, digits)
        return combinations

    def doCombination(self, track: list, combinations: List[int], digits):
        # 触发条件
        if len(digits) == len(track):
            combinations.append("".join(track))
            return
        curdigits = int(digits[len(track)])
        letters = self.keys[curdigits]
        for i in letters:
            # 做选择
            track.append(i)
            self.doCombination(track, combinations, digits)
            # 撤销选择
            track.pop()
