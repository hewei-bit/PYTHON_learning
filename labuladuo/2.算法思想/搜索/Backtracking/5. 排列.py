"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        def backtrack(nums: List[int], track: List[int], res: List[List[int]]):
            # 触发条件

            if len(track) == len(nums):
                res.append(track[:])
                return
            for num in nums:
                # 排除不合法
                if num in track:
                    continue
                # #做选择
                track.append(num)
                backtrack(nums, track, res)
                # 撤销选择
                track.pop()

        backtrack(nums, track, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
