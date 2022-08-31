"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        hashmap = {}
        
        def dfs(n):
            if n is None:
                return None

            new = Node(n.val)
            hashmap[n] = new
            
            neighbors = []
            
            for i in n.neighbors:
                if i not in hashmap:
                    new.neighbors.append(dfs(i))
                else:
                    new.neighbors.append(hashmap[i])
            
            return new
        
        head = dfs(node)
        return head