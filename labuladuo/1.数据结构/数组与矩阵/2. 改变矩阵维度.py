'''
566. Reshape the Matrix (Easy)

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix \
into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r\
 and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix \
in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, \
output the new reshaped matrix; Otherwise, output the original matrix.

'''


class Solution:
    def matrixReshape(self, nums: list, r: int, c: int) -> list:
        m = len(nums)
        n = len(nums[0])

        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]

        index = 0

        for i in range(r):
            for j in range(c):
                ans[i][j] = nums[index // n][index % n]
                index += 1

        return ans


aaa = [[0, 1, 2], [1, 2, 3]]
ans = Solution().matrixReshape(aaa, 1, 6)
print(ans)
