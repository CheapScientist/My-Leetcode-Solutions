// https://leetcode.com/problems/remove-covered-intervals

class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x: (x[0], -x[1]))
        n = len(A)
        ans, rmax = n, A[0][1]
        for i in range(1, n):
            if A[i][1] <= rmax:
                ans -= 1
            else:
                rmax = max(rmax, A[i][1])
        return ans