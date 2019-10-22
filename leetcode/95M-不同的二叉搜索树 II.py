# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generate(l,r):
            if l > r:
                return [None,]
            fina = []
            for i in range(l, r+1):
                l_tree = generate(l,i-1)
                r_tree = generate(i+1, r)
                
                for a in l_tree:
                    for b in r_tree:
                        cur_tree = TreeNode(i)
                        cur_tree.left = a
                        cur_tree.right = b
                        fina.append(cur_tree)
            return fina
        return generate(1, n) if n else []
            