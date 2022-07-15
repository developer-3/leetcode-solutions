class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        mid = len(nums) // 2
        
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return mid + self.search(nums[mid:], target)
        else:
            return self.search(nums[:mid], target)