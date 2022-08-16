// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible

class Solution:
    def minOperations(self, A: List[int], numsDivide: List[int]) -> int:
        g = reduce(gcd, numsDivide)
        for i,a in enumerate(sorted(A)):
            if g % a == 0: return i
            if a > g: break
        return -1