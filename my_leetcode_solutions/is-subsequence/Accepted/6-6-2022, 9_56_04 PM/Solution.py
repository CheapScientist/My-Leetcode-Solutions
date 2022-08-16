// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        i, j = 0, 0  # i points at s, j points at t
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s):
                return True
        return False
        
        