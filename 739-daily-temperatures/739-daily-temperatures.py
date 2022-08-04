class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][0]:
                prev = stack.pop()
                res[prev[1]] = (i - prev[1])
                
            stack.append((temp, i))
        
        return res
                