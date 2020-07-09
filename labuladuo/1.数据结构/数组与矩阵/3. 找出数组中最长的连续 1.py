'''
485. Max Consecutive Ones (Easy)

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max = 0
        count = 0
        for i in range(len(nums)):
            if count > max:
                max = count
            elif nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                count = 0
        max = count if count >max else max
        return max
