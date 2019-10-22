# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.is_true = True
        #l,r = 0,0
        def recu(node):
            if node is None:return 0
            l = recu(node.left) + 1
            r = recu(node.right) + 1
            if abs(l - r) > 1:
                self.is_true = False
            return max(l,r)
        recu(root)
        return self.is_true
        