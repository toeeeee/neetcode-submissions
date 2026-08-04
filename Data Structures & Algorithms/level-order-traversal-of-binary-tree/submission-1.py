# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        trav = []

        Li = collections.deque()
        Li.append(root)

        while Li:
            qLen = len(Li)
            vals = []
            for i in range(qLen):
                node = Li.popleft()
                if node:
                    vals.append(node.val)
                    Li.append(node.left)
                    Li.append(node.right)
            if vals:
                trav.append(vals)

        return trav    

        
    
        