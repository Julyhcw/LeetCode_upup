# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        '''递归'''
        fina = []
        def recru(node):
            if node is None:return None
            fina.append(node.val)
            recru(node.left)
            recru(node.right)
        recru(root)
        return len(set(fina))==1
           
        # '''迭代'''
        # nums = [root]
        # while nums:
        #     tmp = nums.pop()
        #     if tmp.left:
        #         if tmp.val != tmp.left.val:
        #             return False
        #         nums.append(tmp.left)
        #     if tmp.right:
        #         if tmp.val != tmp.right.val:
        #             return False
        #         nums.append(tmp.right)
        # return True
            
            