// https://leetcode.com/problems/teemo-attacking

class Solution:
    def findPoisonedDuration(self, A: List[int], duration: int) -> int:
        if len(A) == 1: return duration
        ans = 0
        for i in range(1, len(A)):
            diff = A[i] - A[i - 1]
            ans += min(diff, duration)
        return ans + duration