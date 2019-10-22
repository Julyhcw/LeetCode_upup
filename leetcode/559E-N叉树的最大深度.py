"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        '''递归'''
#         if root is None:return 0
#         child = [self.maxDepth(i) for i in root.children]
#         if child:
#             return max(child)+1
#         return 1
        '''迭代bfs'''
#         if root is None:return 0
#         queue = []
#         queue.append(root)
#         fina = 0
#         level = 1
#         while queue:
#             tmp = queue.pop(0)
#             level -= 1
#             if tmp.children:
#                 queue.extend(tmp.children)
#             if level == 0:
#                 fina += 1
#                 level = len(queue)

#         return fina
           '''迭代dfs'''
        if root is None:
            return 0
        stack = [(1, root)]
        max_depth = 1
        while stack:
            cur_depth, node = stack.pop()
            max_depth = max(max_depth, cur_depth)
            for i in range(len(node.children)-1, -1, -1):
                if node.children[i]:
                    stack.append((cur_depth+1, node.children[i]))
        return max_depth


            
            
            
            
            
            
            
            
            
            
