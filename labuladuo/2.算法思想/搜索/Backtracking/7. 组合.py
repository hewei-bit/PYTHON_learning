"""
77. Combinations (Medium)

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        combineList = []
        self.backtrack(combineList, combinations, 1, n, k)
        return combinations

    def backtrack(self, combineList: List, combinations: List, start: int, n: int, k: int):
        if k == len(combineList):
            combinations.append(combineList[:])
            return

        for i in range(start, n+1):
            combineList.append(i)
            self.backtrack(combineList, combinations, i + 1, n, k)
            combineList.pop()


if __name__ == '__main__':
    n = 4
    k = 2

    obj = Solution().combine(n, k)
    print(obj)
