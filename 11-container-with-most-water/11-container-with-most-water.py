class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l, r = 0, len(height)-1
        
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            maximum = max(maximum, w*h)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maximum