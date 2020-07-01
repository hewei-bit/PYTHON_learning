"""
213. House Robber II (Medium)


"""
from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        return max(self.myrob(nums[1:]), self.myrob(nums[:-1]))

    def myrob(self, nums: List):
        cur, pre = 0, 0
        for num in nums:
            temp = cur
            cur = max(pre + num, cur)
            pre = temp

        return cur


class Solution2:
    def rob(self, nums: List[int]) -> int:
        def robmax(nums):
            nums_len = len(nums)
            if not nums: return 0
            if nums_len == 1: return nums[0]

            opt = [0] * nums_len
            opt[0] = nums[0]
            opt[1] = max(nums[0], nums[1])

            for i in range(2, nums_len):
                opt[i] = max(opt[i - 1], opt[i - 2] + nums[i])
            return opt[nums_len - 1]

        if not nums: return 0
        if len(nums) == 1: return nums[0]

        nums1 = nums[1:]  # [1,n] 找到到最大值
        nums2 = nums[0:len(nums) - 1]  # [0,n-1] 找到到最大值
        return max(robmax(nums1), robmax(nums2))




if __name__ == '__main__':
    l = [2, 3, 2]
    obj = Solution1().rob(l)
    print(obj)
