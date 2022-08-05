class Solution:
    def dfs(self, grid, visited, r, c, n, m):
        res = [0]
        
        def helper(i, j):
            if grid[i][j] ==  0:
                return
            
            if (i, j) in visited:
                return 
            
            if grid[i][j] == 1:
                visited[(i, j)] = True
                res[0] += 1
            
            # up
            if i > 0:
                helper(i-1, j)
                
            if j < m-1:
                helper(i, j+1)
                
            #down
            if i < n - 1:
                helper(i+1, j)
                
            # left
            if j > 0:
                helper(i, j-1)
        
        helper(r, c)
        return [visited, res]
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = defaultdict(set)
        
        res = 0
        
        for r in range(n):
            for c in range(m):
                if (r,c) not in visited and grid[r][c] == 1:
                    # search for island size
                    search = self.dfs(grid, visited, r, c, n, m)
                    visited = search[0]
                    res = max(res, search[1][0])


        return res
        