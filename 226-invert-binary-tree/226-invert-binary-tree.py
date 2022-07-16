# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        right, left = None, None
        if root.left == None and root.right == None:
            return root
        if root.left != None:
            left = self.invertTree(root.left)
        if root.right != None:
            right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root