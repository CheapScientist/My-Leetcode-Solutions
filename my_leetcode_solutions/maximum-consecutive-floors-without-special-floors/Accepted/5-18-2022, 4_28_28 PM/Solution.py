// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        diff = []
        special.sort()
        diff.append(special[0] - bottom)
        diff.append(top - special[-1])
        for i in range(1, len(special)):
            diff.append(special[i] - special[i - 1] - 1)
        return max(diff)
        
        