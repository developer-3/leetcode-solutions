class Solution:
    def update_array(self, l, r, chars) -> List[str]:
        # compute number of repeated characters
        num = r - l
        
        # if greater than 1 char, remove extra characters
        if num > 1:
            del chars[l+1:r]

            # insert num into array
            num = str(num)
            for n in range(len(num)):
                chars.insert(l+n+1, num[n])
        
        return chars
    
    
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)
        
        l, r = 0, 1
        
        while r != len(chars):
            if chars[l] == chars[r]:
                r += 1
            else:
                chars = self.update_array(l, r, chars)
                
                # update pointers
                if r - l > 1:
                    l = l + 2
                    r = l + 1
                else:
                    l = l + 1
                    r = l + 1
                    
        chars = self.update_array(l, r, chars)
        
        return len(chars)