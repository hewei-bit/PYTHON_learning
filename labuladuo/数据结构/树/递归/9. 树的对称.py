"""
101. Symmetric Tree (Easy)

给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def isSymmetric2(t1:TreeNode,t2:TreeNode):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return isSymmetric2(t1.left,t2.right) and isSymmetric2(t1.right,t2.left)
        return isSymmetric2(root.left,root.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(20)
    root.right = TreeNode(20)
    #root.right.right = TreeNode(7)
    #root.right.left = TreeNode(15)

    print(Solution().isSymmetric(root))
