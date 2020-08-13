"""
547. Friend Circles (Medium)

班上有N名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B的朋友，B 是 C的朋友，那么我们可以认为 A 也是 C的朋友。
所谓的朋友圈，是指所有朋友的集合。

给定一个N * N的矩阵M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。

示例 1:
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]

输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。

"""
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        count = 0
        visited = set()

        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(N):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)

        return count


if __name__ == '__main__':
    ll = [[1, 1, 0],
          [1, 1, 0],
          [0, 0, 1]]
    print(Solution().findCircleNum(ll))
