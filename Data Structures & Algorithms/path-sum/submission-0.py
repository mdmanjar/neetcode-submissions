# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:

        def dfs(root,target):
            if root is None:return False
            if root.left is None and root.right is None:
                return target-root.val==0
            return dfs(root.left,target-root.val) or dfs(root.right,target-root.val)
        return dfs(root,target)
        