from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        resls = []
        stack, node = [], root
        while stack or node:
            while node:
                resls.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return resls
