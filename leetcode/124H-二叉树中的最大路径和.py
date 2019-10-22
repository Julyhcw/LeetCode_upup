# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def help(node):
            if not node:return 0
            l = help(node.left)
            r = help(node.right)
            self.res = max(l + r + node.val, self.res)
            return max(0, max(l, r) + node.val)
        help(root)
        return self.res