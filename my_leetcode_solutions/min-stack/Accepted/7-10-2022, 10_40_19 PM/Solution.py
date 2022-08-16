// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.A, self.B = [], []

    def push(self, val: int) -> None:
        self.A.append(val)
        if not self.B or self.B[-1] >= val: 
            self.B.append(val)
        return
    def pop(self) -> None:
        if not (self.A and self.B):
            return -1 
        if self.A[-1] == self.B[-1]:
            self.A.pop()
            self.B.pop()
        else:
            self.A.pop()

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