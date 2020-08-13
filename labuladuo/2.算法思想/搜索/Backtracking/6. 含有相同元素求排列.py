"""
47. Permutations II (Medium)
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []
        nums.sort()
        hasvisited = [0] * len(nums)
        self.backtrack(track, res, nums, hasvisited)
        return res

    def backtrack(self, track: List[int], res: List[List[int]], nums: List[int], hasvisited: List):
        if len(track) == len(nums):
            res.append(track[:])
            return
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and hasvisited[i - 1] != 0:
                continue
            if hasvisited[i]:
                continue
            hasvisited[i] = True
            track.append(nums[i])
            self.backtrack(track, res, nums, hasvisited)
            track.pop()
            hasvisited[i] = False


if __name__ == '__main__':
    nums = [1, 1, 2]
    obj = Solution().permuteUnique(nums)
    print(obj)