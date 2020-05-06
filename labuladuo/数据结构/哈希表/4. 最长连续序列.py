"""
128. Longest Consecutive Sequence (Hard)
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

"""
import collections

class Solution:
    def longestConsecutive(self, nums: list) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num - 1 in s:
                continue
            curLen = 1
            while num + 1 in s:
                curLen += 1
                num += 1
            res = max(res, curLen)
        return res


class DSU:
    def __init__(self, nums):
        self.pre = {num: num for num in nums}
        self.rank = collections.defaultdict(lambda: 1)
        self.cnt = collections.defaultdict(lambda: 1)

    def find(self, x):
        while x != self.pre[x]:
            x = self.pre[x]
        return x

    def merge(self, x, y):
        if y not in self.pre:
            return 1
        root1, root2 = self.find(x), self.find(y)
        if root1 == root2:
            return self.cnt[root1]
        if self.rank[root1] < self.rank[root2]:
            self.pre[root1] = root2
            self.cnt[root2] += self.cnt[root1]
            return self.cnt[root2]
        elif self.rank[root1] > self.rank[root2]:
            self.pre[root2] = root1
            self.cnt[root1] += self.cnt[root2]
            return self.cnt[root1]
        else:
            self.pre[root1] = root2
            self.cnt[root2] += self.cnt[root1]
            self.rank[root2] += 1
            return self.cnt[root2]


class Solution2:
    def longestConsecutive(self, nums: list) -> int:
        dsu = DSU(nums)
        res = 0
        for num in nums:
            res = max(res, dsu.merge(num, num + 1))
        return res
