class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                curr = stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, i - stack[len(stack)-1])
                
        return res