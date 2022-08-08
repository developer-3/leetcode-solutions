class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 0
        
        for bit in list(bin(n)[2:]):
            x += int(bit) & 1
            
        return x