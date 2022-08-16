// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        n = len(A)
        if n <= 1: return 0
        A.sort(key = lambda x: x[0])
        ans = [A[0]]
        res = 0
        for i in range(1, n): 
            prevstart, prevend = ans[-1]
            start, end = A[i]
            # if they do not overlap: 
            if start > prevend: 
                ans.append(A[i])
            elif start == prevend: 
                ans.pop()
                ans.append([prevstart, end])
            else:
                res += 1
                ans.pop()
                ans.append([max(start, prevstart), min(end, prevend)])
        return res
                