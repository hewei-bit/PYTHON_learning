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
        size = len(nums)
        used = [False for _ in range(size)]
        depth = 0
        path = []

        #路径：记录在track中
        #选择列表：nums中不存在于track的那些元素
        #结束条件：nums中的元素全都在track中出现
        def dfs(nums: List[int], path: List[int], used: List, depth: int, size: int, res: List[int]):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                #排除已做选择
                if not used[i]:
                    #做选择
                    used[i] = True
                    path.append(nums[i])
                    #进入下一层
                    dfs(nums, path, used, depth + 1, size, res)
                    #撤销选择
                    used[i] = False
                    path.pop()

        dfs(nums, path, used, depth, size, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
