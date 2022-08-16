// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def dfs(i, j):
            if i == n or j == m:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            else:
                return max(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
        return dfs(0, 0)