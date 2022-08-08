class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]

        
        return sum([int(x) for x in list(n)])