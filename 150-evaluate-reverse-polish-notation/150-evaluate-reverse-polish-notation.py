class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if not t.strip('-').isnumeric():
                n1 = stack.pop()
                n2 = stack.pop()
                
                res = 0
                match t:
                    case "+": res = int(n1) + int(n2)
                    case "-": res = int(n2) - int(n1)
                    case "*": res = int(n1) * int(n2)
                    case "/": res = int(int(n2) / int(n1))
                
                stack.append(str(res))
            else:
                stack.append(t)

        return stack.pop()