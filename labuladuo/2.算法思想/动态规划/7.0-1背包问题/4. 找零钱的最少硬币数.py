"""
322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回-1。

示例1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1


"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount +1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins
                if(i - coin) < 0:
                    continue
                dp[i] = min(dp[i],1+dp[i - coin])
        return -1 if
