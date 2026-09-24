"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent=None

        def find_parent(root,pr):
            nonlocal parent
            if root is None:return
            if root.parent is None:
                parent=root
                return
            if root.left is not pr:find_parent(root.left,root)
            if root.right is not pr:find_parent(root.right,root)
            if root.parent is not pr:find_parent(root.parent,root)

        find_parent(p or q,None)

        def dfs(root):
            if root is None:return None
            if root in (p,q):return root
            left=dfs(root.left)
            right=dfs(root.right)
            if left and right:return root
            return left or right
        return dfs(root)




            
        