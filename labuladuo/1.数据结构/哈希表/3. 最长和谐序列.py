"""
594. Longest Harmonious Subsequence (Easy)
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
示例 1:
输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.

"""


class Solution:
    def findLHS(self, nums: list) -> int:
        hashlist = {}
        for i in nums:
            if i not in hashlist:
                hashlist[i] = 1
            else:
                hashlist[i] += 1
        res = 0
        for i in hashlist:
            if i + 1 in hashlist:
                up = hashlist[i + 1]
                res = max(res, up + hashlist[i])
        return res


aaa = [1, 3, 2, 2, 5, 2, 3, 7]
obj = Solution().findLHS(aaa)
