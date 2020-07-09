"""
217. Contains Duplicate (Easy)

给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true
示例 2:
输入: [1,2,3,4]
输出: false

"""


class Solution:
    def containsDuplicate1(self, nums: list) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums: list) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return True
        return False

    # 哈希表
    def containsDuplicate3(self, nums: list) -> bool:
        dic = {}
        for i in nums:
            if dic.get(i):
                return True
            dic[i] = 1
        return False
