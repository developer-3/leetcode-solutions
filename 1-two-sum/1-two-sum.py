class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, x in enumerate(nums):
            if x not in hashMap: hashMap[target - x] = i
            else: return [i, hashMap[x]]