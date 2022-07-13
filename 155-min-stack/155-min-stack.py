class MinStack:

    def __init__(self):
        self.currMin = []
        self.stack = []

    def push(self, val: int) -> None:
        self.currMin.append(val)
        self.currMin = sorted(self.currMin)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.currMin.remove(popped)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()