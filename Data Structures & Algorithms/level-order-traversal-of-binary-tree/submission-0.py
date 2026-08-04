# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        trav = []
        Li = [root]
        trav.append([root.val])

        while Li:
            Lnext = []
            vals = []
            for node in Li:
                edges = [node.left, node.right] 
                if not edges:
                    return trav
                for edge in edges:
                    if edge:
                        Lnext.append(edge)
                        vals.append(edge.val)
            if vals:
                trav.append(vals)
            Li = Lnext
        return trav    

        
    
        