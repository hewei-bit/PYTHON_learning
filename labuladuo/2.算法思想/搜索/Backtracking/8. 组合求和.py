"""
39. Combination Sum (Medium)
给定一个无重复元素的数组candidates和一个目标数target，
找出candidates中所有可以使数字和为target的组合。

candidates中的数字可以无限制重复被选取。

说明：

所有数字（包括target）都是正整数。
解集不能包含重复的组合。
示例1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        self.backtrack(track, res, 0, target, candidates)
        return res

    def backtrack(self, track: List[int], res: List[int], start: int, target: int, candidates: List):
        if target == 0:
            res.append(track[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                track.append(candidates[i])
                self.backtrack(track, res, i, target - candidates[i], candidates)
                track.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
