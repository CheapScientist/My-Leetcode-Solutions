// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k =len(s1), len(s2), len(s3)
        if n + m != k: 
            return False
        
        @cache
        def dfs(i, j):
            if i == n and j == m: 
                return True
            if (i < n and s3[i + j] != s1[i]) and (j < m and s3[i + j] != s2[j]):
                return False
            if i < n and s1[i] == s3[i+j]:
                if dfs(i + 1, j): 
                    return True
            if j < m and s2[j] == s3[i+j]:
                if dfs(i, j + 1):
                    return True
            return False
        
        return dfs(0, 0)
            