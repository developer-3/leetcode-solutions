# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        
        res = [[root.val]]
        
        while q:
            level = []
            temp = []
            
            for n in q:
                if n.left is not None:
                    level.append(n.left.val)
                    temp.append(n.left)

                if n.right is not None:
                    level.append(n.right.val)
                    temp.append(n.right)
                    
            if level != []:
                res.append(level)
            q.clear()
            for n in temp:
                q.append(n)
                
            
        return res