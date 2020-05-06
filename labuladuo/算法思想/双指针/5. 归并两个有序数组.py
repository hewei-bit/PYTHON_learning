"""
88. Merge Sorted Array (Easy)
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif m == 0:
            nums1[:n] = nums2[:n]
        else:
            a, b = m - 1, n - 1
            k = m + n - 1
            while a >= 0 and b >= 0:
                if nums1[a] > nums2[b]:
                    nums1[k] = nums1[a]
                    a -= 1
                    k -= 1
                else:
                    nums1[k] = nums2[b]
                    b -= 1
                    k -= 1
            if a >= 0:
                pass
            if b >= 0:
                nums1[k - b:k + 1] = nums2[:b + 1]


a = [1, 2, 5, 0, 0, 0]
b = [2, 3, 4]
Solution().merge(a, 3, b, 3)
print(a)
