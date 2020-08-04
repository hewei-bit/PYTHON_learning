"""
695. Max Area of Island (Medium)

给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

 

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

"""

"""回溯算法 """
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        if m == 0:
            return 0
        ans = 0

        def dfs(i, j):
            # 超出范围，排除不合法
            if i < 0 or i >= m or j < 0 or j >= n: return 0
            if grid[i][j] == 0: return 0
            grid[i][j] = 0
            # 做选择
            top = dfs(i + 1, j)
            bottom = dfs(i - 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            return 1 + sum([top, bottom, left, right])

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ is '__main__':
    grid = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    solution = Solution()
    res = solution.maxAreaOfIsland(grid)
    print(res)
