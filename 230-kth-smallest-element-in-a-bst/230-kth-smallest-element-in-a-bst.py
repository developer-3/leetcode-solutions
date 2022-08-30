# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def listify(root):
            if not root:
                return None
            
            l = listify(root.left)
            r = listify(root.right)
            
            if not l and not r:
                return [root.val]
            elif not l:
                return [root.val] + r
            elif not r:
                return [root.val] + l
            else:
                return [root.val] + l + r
            
        l = listify(root)
        
        heap = heapq.heapify(l)
        
        for i in range(k-1):
            heapq.heappop(l)
            
        return heapq.heappop(l)
            