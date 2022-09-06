# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def pre(node):
            if not node:
                return None
            
            res.append(node.val)
            
            l = pre(node.left)
            r = pre(node.right)
            
            
        pre(root)
        return res