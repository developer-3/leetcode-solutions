class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        index = len(digits)-1
        cur = 9
        while cur == 9:
            if index == 0:
                digits[index] = 0
                digits.insert(0, 1)
                return digits
            
            digits[index] = 0
            index -= 1
            cur = digits[index]
            
        digits[index] += 1
            
        return digits