"""
633. Sum of Square Numbers (Easy)
给定一个非负整数c，你要判断是否存在两个整数 a 和 b，使得a2 + b2 = c。

示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5

示例2:
输入: 3
输出: False
"""

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if 0 > c:
            return False
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            powsum = i * i + j * j
            if powsum == c:
                return True
            elif powsum > c:
                j = j - 1
            else:
                i = i + 1
        return False


aaa = Solution()
bbb = aaa.judgeSquareSum(2)
print(bbb)
