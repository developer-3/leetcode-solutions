class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(list)
        
        for n in nums:
            hashmap[n].append(n)
            
        vals = sorted(hashmap.values(), key=len, reverse=True)[:k]
        
        return [n[0] for n in vals]
                
        