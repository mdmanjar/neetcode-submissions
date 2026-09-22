# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i=j=0

        def dfs(stop):
            nonlocal i,j
            if i>=len(preorder):return None

            if stop==inorder[j]:
                j+=1
                return None

            node=TreeNode(preorder[i])
            i+=1
            node.left=dfs(node.val)
            node.right=dfs(stop)
            return node
        return dfs(math.inf)

        