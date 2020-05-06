class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        # 建树
        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                tmp = num & 1 << i
                if tmp:
                    if not cur.one:
                        cur.one = TrieNode()
                    cur = cur.one
                else:
                    if not cur.zero:
                        cur.zero = TrieNode()
                    cur = cur.zero
        # 找最大值
        res = 0
        for num in nums:
            cur = root
            val = 0
            for i in range(31, -1, -1):

                tmp = num & 1 << i
                if cur.zero and cur.one:
                    if tmp:
                        cur = cur.zero
                    else:
                        cur = cur.one
                    val += 1 << i
                else:
                    if (cur.zero and tmp) or (cur.one and not tmp):
                        val += 1 << i
                    cur = cur.one or cur.zero
            res = max(res, val)
        return res


obj = Solution()
bbb = [1, 2, 3, 4]
aaa = obj.findMaximumXOR(bbb)
