# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True

        def dfs(root):
            nonlocal ans 
            if not root:return 0
            l=dfs(root.left)
            r=dfs(root.right)
            diff=l-r
            if not(-1<=diff<=1):
                ans=False

            return max(l,r)+1
        dfs(root)
        return ans


        