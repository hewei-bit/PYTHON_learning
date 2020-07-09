'''
283. Move Zeroes (Easy)

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

'''快慢双指针'''


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = nums[:]
        j = 0

        for i in range(len(nums)):
            if num[i] != 0:
                nums[j] = num[i]
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1


'''双指针'''


class Solution2:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素
        # i 为慢指针 指向最新一个0元素的位置
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


nums = [0, 1, 2, 0, 3]
obj = Solution().moveZeroes(nums)
print(nums)
