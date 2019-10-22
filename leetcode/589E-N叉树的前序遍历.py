"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''迭代'''
        if root is None:return None
        nums = [root]
        fina = []
        while nums:
            tmp = nums.pop()
            fina.append(tmp.val)
            nums.extend(tmp.children[::-1])
        return fina                    
           
        # '''递归'''
        # fina = []
        # def front(node):
        #     if node is None:return None
        #     fina.append(node.val)
        #     for i in node.children:
        #         front(i)
        #     #return self.fina
        # front(root)
        # return fina