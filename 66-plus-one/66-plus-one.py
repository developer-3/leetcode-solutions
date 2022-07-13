class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert the list to a integer
        num = 0
        for i in range(len(digits)):
            num += 10**i * digits[::-1][i]
        
        # Add one to the number and convert it back to a list
        return list(str(num + 1))