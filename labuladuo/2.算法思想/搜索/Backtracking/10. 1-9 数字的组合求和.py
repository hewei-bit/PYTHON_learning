"""
216. Combination Sum III (Medium)

找出所有相加之和为n 的k个数的组合。
组合中只允许含有 1 -9 的正整数，
并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]

"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        track = []
        self.backtrack(track, res, k, n, 1)
        return res

    def backtrack(self, track, res, k, n, start):
        if k == 0 and n == 0:
            res.append(track[:])
            return
        if k == 0 or n == 0:
            return
        for i in range(start, 10):
            track.append(i)
            self.backtrack(track, res, k - 1, n - i, i + 1)
            track.pop()


if __name__ == '__main__':
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))
