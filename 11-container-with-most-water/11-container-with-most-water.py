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
            
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         w = j - i
        #         h = min(height[i], height[j])
        #         maximum = max(maximum, w*h)
                
        return maximum