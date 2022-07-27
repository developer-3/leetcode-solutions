class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r] + nums[i]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                elif curr == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
        
        return res