"""
198. House Robber (Easy)
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

"""


class Solution:
    def rob(self, nums: list) -> int:

        N = len(nums)
        if N == 0:
            return 0
        robbed = [0] * (N + 1)
        robbed[0] = 0
        robbed[1] = nums[0]
        for i in range(2, N + 1):
            robbed[i] = max(robbed[i - 1], robbed[i - 2] + nums[i - 1])
        return robbed[N]

    def rob2(self, nums: list) -> int:
        pre1 = 0
        pre2 = 0
        for i in range(len(nums)):
            cur = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return pre1



