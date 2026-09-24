# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(root,key):
            if root is None:return None
            if key<root.val:
                root.left=delete(root.left,key)
            elif key>root.val:
                root.right=delete(root.right,key)
            if root.val==key:
                if root.left is None:return root.right
                if root.right is None:return root.left
                
                left=root.left
                while left.right:
                    left=left.right
                root.left=delete(root.left,left.val)
                root.val=left.val

            return root

        return delete(root,key)
            

        