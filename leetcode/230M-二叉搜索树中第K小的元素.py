# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
         ans = []
         def front_trick(node):
            if node is None:return
            front_trick(node.left)
            ans.append(node.val)
            front_trick(node.right)
         front_trick(root)
         return ans[k-1]