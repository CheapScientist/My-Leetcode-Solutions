// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, A: List[int], i: int) -> bool:
        if 0 <= i < len(A) and A[i] >= 0:
            A[i] = -A[i]
            return A[i] == 0 or self.canReach(A, i + A[i]) or self.canReach(A, i - A[i])
        return False
        