class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        
        currSub = ""
        for c in s:
            if c in currSub:
                index = currSub.index(c)
                currSub = currSub[index+1:] if index+1 != len(currSub) else ""
                currSub += c
            else:
                currSub += c
            
            longest = max(currSub, longest, key=len)
            
        return len(longest)