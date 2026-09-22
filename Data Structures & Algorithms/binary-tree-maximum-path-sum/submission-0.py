# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-math.inf

        def dfs(root):
            nonlocal ans

            if root is None:return 0
            left=max(0,dfs(root.left))
            right=max(0,dfs(root.right))
            ans=max(ans,root.val+left+right)
            return max(left,right)+root.val
        dfs(root)
        return ans
        