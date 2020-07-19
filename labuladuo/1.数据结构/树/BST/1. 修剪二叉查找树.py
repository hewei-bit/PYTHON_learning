"""
669. Trim a Binary Search Tree (Easy)

给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，
使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例 1:

输入:
    1
   / \
  0   2

  L = 1
  R = 2

输出:
    1
      \
       2

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:return None
        if root.val > R:return self.trimBST(root.left,L,R)
        if root.val < L:return self.trimBST(root.right,L,R)

        root.left = self.trimBST(root.left,L,R)

        root.right = self.trimBST(root.right,L,R)
        return root

if __name__ == '__main__':
    a = TreeNode(1)
    c = TreeNode(0)
    b = TreeNode(2)
    a.left = c
    a.right = b
    Solution().trimBST(a,1,2)


