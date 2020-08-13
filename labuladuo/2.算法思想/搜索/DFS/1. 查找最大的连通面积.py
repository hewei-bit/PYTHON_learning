"""
695. Max Area of Island (Medium)

给定一个包含了一些 0 和 1 的非空二维数组grid 。

一个岛屿是由一些相邻的1(代表土地) 构成的组合，
这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设grid 的四个边缘都被 0（代表水）包围着。

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
对于上面这个给定矩阵应返回6。注意答案不应该是 11 ，
因为岛屿只能包含水平或垂直的四个方向的 1 。

"""

"""回溯算法 """
from typing import List


class Solution:
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m, n = 0, 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.m = len(grid)
        self.n = len(grid[0])
        if self.m == 0:
            return 0
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(grid, i, j))
        return ans

    def dfs(self, grid: List[List[int]], i, j):
        # global m, n
        # 超出范围，排除不合法
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        # 做选择
        area = 1
        for direct in self.direction:
            area += self.dfs(grid, i + direct[0], j + direct[1])
        return area


if __name__ is '__main__':
    grid = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    print("res : %d " % Solution().maxAreaOfIsland(grid))
