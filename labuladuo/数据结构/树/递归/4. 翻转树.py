"""
226. Invert Binary Tree (Easy)
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root



    def invertTree3(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

    print(Solution().invertTree(root))
