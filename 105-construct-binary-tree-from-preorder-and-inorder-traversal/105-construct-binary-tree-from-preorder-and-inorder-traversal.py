# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(ino, pre):
            if len(ino) == 1:
                return TreeNode(val=ino[0])
            elif len(ino) < 1:
                return None
            
            root = None
            for n in pre:
                if n not in ino:
                    continue
                else:
                    root = n
                    break
             
            root_index = ino.index(root)
            l = ino[:root_index]
            r = ino[root_index+1:]
            
            r_pre_idx = pre.index(root)
            pre = pre[r_pre_idx:]
            
            left = build(l, pre)
            right = build(r, pre)
            
            node = TreeNode(val=root, left=left, right=right)
            
            return node
        
        head = build(inorder, preorder)
        return head
            