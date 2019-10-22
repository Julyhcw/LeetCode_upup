"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
       
        '''迭代'''
        if root is None:return None
        fina = []
        nums = [root]
        n = 1
        while nums:
            res = []
            m = 0
            #tmp = nums.pop(0)
            for i in range(n):
                tmp = nums.pop(0)
                for child in tmp.children:
                    nums.append(child)
                    m += 1
                res.append(tmp.val)
            fina.append(res)
            n = m               
        return fina
        