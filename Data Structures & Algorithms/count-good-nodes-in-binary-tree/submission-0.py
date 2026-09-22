# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,mx):
            if root is None:return 0
            ans=0
            if root.val>=mx:ans+=1
            mx=max(root.val,mx)
            return dfs(root.left,mx)+dfs(root.right,mx)+ans
        return dfs(root,-200)

        