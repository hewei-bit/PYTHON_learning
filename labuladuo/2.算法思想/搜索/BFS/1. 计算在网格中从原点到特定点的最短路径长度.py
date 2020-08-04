"""
1091. Shortest Path in Binary Matrix(Medium)

在一个 N × N 的方形网格中，每个单元格有两种状态：
空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，
由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通
（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空
（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。
如果不存在这样的路径，返回 -1 。


"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: list) -> int:
        n = len(grid)
        m = len(grid[0])
        can_visit = {(x, y) for x in range(n) for y in range(m) if grid[x][y] == 0}
        direction = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == 0 and y == 0)]
        queue = set()
        if grid[0][0] == 0:
            queue.add((0, 0))
        k = 0
        while queue:
            k += 1
            new = set()
            for x, y in queue:
                if (x, y) == (n - 1, m - 1):
                    return k
                for dx, dy in direction:
                    if (x + dx, y + dy) in can_visit:
                        new.add((x + dx, y + dy))
                        can_visit.remove((x + dx, y + dy))
            queue = new
        return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
obj = Solution().shortestPathBinaryMatrix(grid)
print(obj)
