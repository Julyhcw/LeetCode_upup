"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''迭代'''
        if root is None:return None
        nums = [root]
        fina = []
        res = []
        while nums:
            tmp = nums.pop()
            fina.append(tmp)
            nums.extend(tmp.children)
           
        for node in fina[::-1]:
            res.append(node.val)
        return res
            
            
        
        #'''递归'''
        # fina = []
        # def post(node):
        #     if node is None:return None
        #     for child in node.children:
        #         post(child)
        #     fina.append(node.val)
        # post(root)
        # return fina
        