// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        
        @cache
        def dfs(i, j):
            if i == l1 and j == l2:
                return True
            temp = False
            if i < l1 and s1[i] == s3[i + j]:
                temp = temp or dfs(i + 1, j)
            if j < l2 and s2[j] == s3[i + j]:
                temp = temp or dfs(i, j + 1)
            return temp
        
        return dfs(0, 0)
                