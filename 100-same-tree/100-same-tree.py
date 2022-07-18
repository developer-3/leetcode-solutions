# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True
            elif (not p and q) or (not q and p):
                return False
            
            if p.val != q.val:
                return False
            
            r, l = dfs(p.right, q.right), dfs(p.left, q.left)
            
            if l and r:
                return True
            return False
            
        return dfs(p, q)