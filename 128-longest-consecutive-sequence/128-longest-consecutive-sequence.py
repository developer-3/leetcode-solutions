class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashmap = {}
        
        nums = sorted(nums)
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n-1, 0)
            
        return max(hashmap.values())
                