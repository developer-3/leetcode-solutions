class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += 10**i * digits[::-1][i]
            
        num += 1
        
        return list(str(num))