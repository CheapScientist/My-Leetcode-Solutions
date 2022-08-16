// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        n = len(A)
        if n <= 1: return 0
        A.sort(key = lambda x: x[0])
        prev = A[0]
        res = 0
        for i in range(1, n): 
            prevstart, prevend = prev
            start, end = A[i]
            # if they do not overlap: 
            if start > prevend: 
                prev = A[i]
            elif start == prevend: 
                prev = [prevstart, end]
            else:
                res += 1
                prev = [max(start, prevstart), min(end, prevend)]
        return res
                