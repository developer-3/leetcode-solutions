class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse=True)
        
        while len(stones) > 1:
            y, x = stones[0], stones[1]
            if x == y:
                stones = stones[2:]
            else:
                stones = stones[1:]
                stones[0] = y-x
                stones = sorted(stones, reverse=True)
                
        return stones[0] if stones else 0