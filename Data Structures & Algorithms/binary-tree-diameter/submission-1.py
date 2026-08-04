# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(node):
    if not node:
        return 0
    l = height(node.left)
    r = height(node.right)
    return max(l,r) + 1

def diameter(node):
    if not node:
        return 0

    leftpath = height(node.left)
    rightpath = height(node.right)
    curpath = leftpath + rightpath

    # Traverse all nodes BFS and find biggest path
    nextpath = max(diameter(node.left), diameter(node.right))

    return max(curpath, nextpath)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter(root)
        