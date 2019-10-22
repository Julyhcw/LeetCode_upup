# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #ans = 0
        def recur(node):
            if not node:return False
            l = recur(node.left)
            r = recur(node.right)
            mid = node == p or node == q
            if mid + l + r >= 2:
                self.ans = node
            return mid or l or r
        recur(root)
        return self.ans