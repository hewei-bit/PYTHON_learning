"""
230. Kth Smallest Element in a BST (Medium)
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        val = 0

        def inorder(node: TreeNode, k: int):
            if node is None:
                return
            inorder(node.left, k)
            nonlocal cnt
            cnt += 1
            if cnt == k:
                nonlocal val
                val = node.val
                return
            inorder(node.right, k)

        inorder(root, k)
        return val
