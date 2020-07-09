"""
104. Maximum Depth of Binary Tree (Easy)

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)
        # 通过max, 会自动过滤掉深度较小的
        return max(left, right) + 1


# BFS，层次遍历最后得到的深度就是最大的深度
class Solution2:
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
        return depth


# DFS与BFS有两点不同：
# 最后得到的深度不一定是最大深度，所以要用max判断
# DFS（先序遍历）节点右孩子先入栈，左孩子再入栈`
class Solution3:
    def maxDepth(self, root) -> int:
        # DFS
        if root is None:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_dep, node = stack.pop()
            depth = max(depth, cur_dep)
            if node.right:
                stack.append((cur_dep + 1, node.right))
            if node.left:
                stack.append((cur_dep + 1, node.left))
        return depth


class Solution4:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        depth = 0
        depth = self.helper(root, depth)
        return depth

    def helper(self, node, depth):
        if node is None:
            return depth
        depth += 1
        left_lenth = self.helper(node.left, depth)
        right_lenth = self.helper(node.right, depth)

        return max(left_lenth, right_lenth)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

    # obj = Solution().maxDepth(root)
    obj2 = Solution2().maxDepth(root)
    obj3 = Solution3().maxDepth(root)
    # obj4 = Solution4().maxDepth(root)
