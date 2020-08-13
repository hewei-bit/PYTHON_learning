"""
309. 最佳买卖股票时机含冷冻期

给定一个整数数组，其中第i个元素代表了第i天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        dp_pre_0 = 0
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


if __name__ == '__main__':
    l = [1,2,3,0,2]
    obj = Solution().maxProfit(l)
    print(obj)







