class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        close = ")]}"
        
        stack = []
        for p in s:
            if p in op:
                stack.append(p)
                continue
            
            if len(stack) == 0:
                return False
            
            curr = stack.pop()
            if curr == "(" and p == ")":
                continue
            elif curr == "[" and p == "]":
                continue
            elif curr == "{" and p == "}":
                continue
            else:
                return False
        
        return True if len(stack) == 0 else False