// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.all = []
        self.dec = []

    def push(self, val: int) -> None:
        self.all.append(val)
        if not self.dec: 
            self.dec.append(val)
        elif self.dec and self.dec[-1] >= val:
            self.dec.append(val)

    def pop(self) -> None:
        if self.all.pop() == self.dec[-1]:
            self.dec.pop()

    def top(self) -> int:
        return self.all[-1]

    def getMin(self) -> int:
        return self.dec[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()