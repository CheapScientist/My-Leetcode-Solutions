// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.A, self.B = [], []
        

    def push(self, val: int) -> None:
        self.A.append(val)
        if self.B:
            val = min(val, self.B[-1])
        self.B.append(val)
        
    def pop(self) -> None:
        self.A.pop()
        self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.B[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()