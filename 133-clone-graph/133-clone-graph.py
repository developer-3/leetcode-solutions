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
        
        def dfs(n, visited):
            if n is None:
                return None
            visited.add(n.val)
            new = Node(n.val)
            hashmap[n] = new
            
            neighbors = []
            
            for i in n.neighbors:
                if i.val not in visited:
                    new.neighbors.append(dfs(i, visited))
                else:
                    new.neighbors.append(hashmap[i])
            
            return new
        
        head = dfs(node, set())
        return head