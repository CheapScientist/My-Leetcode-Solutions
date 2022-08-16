// https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        prev = []
        res = 0
        
        for i in ops:
            if i == 'C':
                prev = prev[:-1]
            elif i == 'D':
                prev.append(2*prev[-1])
            elif i == '+':
                prev.append(prev[-1] + prev[-2])
            else:
                prev.append(int(i))
        return sum(prev)
        