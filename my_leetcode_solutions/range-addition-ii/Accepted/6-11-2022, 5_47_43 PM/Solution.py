// https://leetcode.com/problems/range-addition-ii

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m*n
        mnx, mny = float('inf'), float('inf')
        for x, y in ops: 
            mnx = min(mnx, x)
            mny = min(mny, y)
        return mnx*mny