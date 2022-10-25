class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n != 1:
            n = list(str(n))
            new = 0
            for i in n:
                new += int(i)**2
                
            n = new
            if n in visited:
                return False
            visited.append(n)
            
        return True
            