"""
279. Perfect Squares (Medium)

Given a positive integer n,
find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...)
which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step

    def __str__(self):
        return '<value:{},step:{}>'.format(self.value, self.step)


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]

