class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        
        def helper(houses):
            r1, r2 = 0, 0
            
            for h in houses:
                temp = max(h + r1, r2)
                r1, r2 = r2, temp
                
            return r2
        
        
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))