# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
            return False
        
        def dfs(root):
            if not root:
                return
            
            r = dfs(root.right)
            l = dfs(root.left)
            if r or l:
                return True
            
            if root.val == subRoot.val:
                return isSameTree(root, subRoot)
            return
            
        return dfs(root)