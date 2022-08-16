// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, A: List[int]) -> int:
        n = len(A)
        if n <= 1: return 0
        l, r, ans = 0, n - 1, 0
        lMax, rMax = A[0], A[-1]
        while l < r:
            if lMax > rMax: 
                r -= 1
                rMax = max(rMax, A[r])
                ans += rMax - A[r]
            else:
                l += 1
                lMax = max(lMax, A[l])
                ans += lMax - A[l]
        return ans