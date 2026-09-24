# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(root,val):
            if root is None:return None
            if val<root.val:
                root.left=delete(root.left,val)
            elif val>root.val:
                root.right=delete(root.right,val)
            if root.val==val:
                if root.left is None:return root.right
                if root.right is None:return root.left
                
                left=root.left
                while left.right:
                    left=left.right
                root.left=delete(root.left,left.val)
                root.val=left.val

            return root

        return delete(root,key)
            

        