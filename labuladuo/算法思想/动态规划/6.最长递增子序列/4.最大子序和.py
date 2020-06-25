"""
53. 最大子序和
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        res = float('-inf')
        for i in range(length):
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    l1 = [1]
    l = [-12, -23, -3, 234, 23, -5]
    obj = Solution().maxSubArray(l)
    print(obj)
