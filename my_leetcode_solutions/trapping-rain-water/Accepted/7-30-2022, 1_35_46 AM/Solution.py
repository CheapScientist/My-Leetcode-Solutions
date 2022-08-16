// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, A: List[int]) -> int:
        if len(A) <= 1: return 0
        n = len(A)
        leftMax, rightMax = [0]*n, [0]*n
        leftMax[0], rightMax[-1] = A[0], A[-1]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], A[i])
        for i in range(n - 2 , -1, -1):
            rightMax[i] = max(rightMax[i + 1], A[i])
        ans = 0 
        for i in range(1, n - 1):
            h = A[i]
            ans += max((min(leftMax[i - 1], rightMax[i + 1]) - h), 0)
        return ans
        