class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 1, 2
        if n == 1:return i
        if n == 2: return j
        
        for _ in range(n-2):
            curr = i + j
            i, j = j, curr
            
        return j