class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def find_pd(l, r, resLen) -> str:
            res = ""
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                    
                r += 1
                l -= 1
                
            return res
        
        
        
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            
            # odd case
            res = max(res, find_pd(i, i, resLen), key=len)
            
            # even case
            res = max(res, find_pd(i, i+1, resLen), key=len)
        

        return res