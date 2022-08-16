// https://leetcode.com/problems/move-pieces-to-obtain-a-string

class Solution:
    def canChange(self, A: str, B: str) -> bool:
        n = len(A)
        j = 0
        for i in range(n):
            if A[i] == '_':
                continue
            while j < n and B[j] == '_':
                j += 1
            if j == n:
                return False
            if A[i] == 'L' and B[j] == 'R':
                return False
            if A[i] == 'R' and B[j] == 'L':
                return False
            if A[i] == 'L' and B[j] == 'L' and i < j:
                return False
            if A[i] == 'R' and B[j] == 'R' and i > j:
                return False
            j += 1
        for k in range(j, n):
            if B[j] != '_':
                return False
        return True